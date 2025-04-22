from pathlib import Path
from parser import parserDisciplina, salvaResultado
from data import historicos
from copy import deepcopy
import fitz
from collections import defaultdict
from data import cco as cco_padrao, sin as sin_padrao  # estado inicial dos dicionários


def disciplinas_viaveis(dicionario):
    viaveis = []

    for id_disc, dados in dicionario.items():
        if dados["situacao"] == 1:
            continue  # já aprovada, não deve ser sugerida

        requisitos = dados["requisito"]
        if requisitos == 0 or requisitos == []:
            viaveis.append(f'{dados["codigo"]} - {dados["nome"]}')
            continue

        # Verifica se todos os pré-requisitos estão aprovados
        todos_aprovados = all(
            isinstance(req_id, str) and dicionario.get(req_id, {}).get("situacao") == 1
            for req_id in requisitos
        )

        if todos_aprovados:
            viaveis.append(f'{dados["codigo"]} - {dados["nome"]}')

    return viaveis


def atualizar_situacoes(path_txt, dicionario):
    with open(path_txt, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas:
        partes = linha.strip().split('|')
        if len(partes) < 5:
            continue

        codigo_raw = partes[1].strip()
        situacao_raw = partes[-1].replace("Situação:", "").strip()

        codigo = codigo_raw.upper()
        situacao = situacao_raw.upper()

        for item in dicionario.values():
            if item["codigo"] == codigo or codigo in item.get("equivalentes", []):
                if situacao == "APR" or situacao == "CUMP":
                    item["situacao"] = 1
                elif situacao.startswith("REP"):
                    item["situacao"] = -1
                break

    return dicionario


def calcular_limite_ch_aprovada(caminho_txt):
    periodos = defaultdict(list)

    with open(caminho_txt, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split("|")
            if len(partes) < 5:
                continue

            ano = partes[0].strip()
            ch_str = partes[3].replace("CH:", "").strip()
            situacao = partes[-1].replace("Situação:", "").strip().upper()

            try:
                ch = int(ch_str)
            except ValueError:
                continue

            periodos[ano].append({"ch": ch, "situacao": situacao})

    ultimos_periodos = sorted(periodos.keys(), reverse=True)[:2]

    ch_total = 0
    ch_aprovada = 0

    for periodo in ultimos_periodos:
        for d in periodos[periodo]:
            ch_total += d["ch"]
            if d["situacao"] == "APR":
                ch_aprovada += d["ch"]

    if ch_total == 0:
        return 0

    percentual = (ch_aprovada / ch_total) * 100
    media_ch_aprovada = ch_aprovada / 2

    if percentual <= 30:
        extra = 0
    elif percentual <= 50:
        extra = 32
    elif percentual <= 80:
        extra = 48
    else:
        extra = 64

    limite_final = int(media_ch_aprovada + extra)

    return {
        "limite_final": limite_final,
        "percentual_aproveitamento": round(percentual, 2),
        "media_aprovada": int(media_ch_aprovada),
        "ch_total": ch_total,
        "ch_aprovada": ch_aprovada,
        "periodos_analisados": ultimos_periodos
    }

def pontuar_disciplinas_viaveis(dicionario, disciplinas_viaveis, periodo_entrada="2022.1", periodo_final="2024.1"):
    def gerar_lista_periodos(inicio, fim):
        anos = range(int(inicio.split('.')[0]), int(fim.split('.')[0]) + 1)
        periodos = []
        for ano in anos:
            for semestre in (1, 2):
                p = f"{ano}.{semestre}"
                periodos.append(p)
                if p == fim:
                    return periodos
        return periodos

    def contar_dependencias(dicionario, id_disciplina, visitados=None):
        if visitados is None:
            visitados = set()
        if id_disciplina in visitados:
            return 0
        visitados.add(id_disciplina)
        total = 0
        for id_, dados in dicionario.items():
            requisitos = dados["requisito"]
            if isinstance(requisitos, list) and id_disciplina in requisitos:
                total += 1 + contar_dependencias(dicionario, id_, visitados)
        return total

    # Transforma a lista 'disciplinas_viaveis' em conjunto de códigos
    codigos_viaveis = set([s.split(" - ")[0] for s in disciplinas_viaveis])

    periodos = gerar_lista_periodos(periodo_entrada, periodo_final)
    periodo_atual = len(periodos)

    resultados = []

    for id_disc, dados in dicionario.items():
        if dados["codigo"] not in codigos_viaveis:
            continue

        obrigatoria = dados.get("obrigatoria", 0)
        impacto_requisitos = contar_dependencias(dicionario, id_disc)
        distancia_periodo = periodo_atual - dados.get("periodo", periodo_atual)
        anual = dados.get("anual", 0)

        nota = obrigatoria * 100 + impacto_requisitos * 10 + distancia_periodo * 5 + anual

        # Atualiza diretamente no dicionário
        dicionario[id_disc]["parametro"] = nota

        resultados.append({
            "codigo": dados["codigo"],
            "nome": dados["nome"],
            "pontuacao": nota,
        })

    return resultados


def funcao_objetivo(dicionario, candidatas, limite_ch):
    # Estratégia gulosa
    disciplinas_info = []
    for id_disc, dados in dicionario.items():
        if dados["codigo"] in candidatas:
            disciplinas_info.append({
                "id": id_disc,
                "codigo": dados["codigo"],
                "ch": int(dados["ch"]),
                "parametro": dados["parametro"]
            })

    # Ordena pela maior razão benefício/custo (parametro)
    disciplinas_info.sort(key=lambda d: d["parametro"], reverse=True)

    ch_total = 0
    pontuacao_total = 0
    selecionadas = []

    for disc in disciplinas_info:
        if ch_total + disc["ch"] <= limite_ch:
            ch_total += disc["ch"]
            pontuacao_total += disc["parametro"]
            selecionadas.append(disc["codigo"])

    return selecionadas, pontuacao_total


if __name__ == "__main__":
    for dataset in historicos:
        caminho = Path(f'../Datasets/{dataset}')
        nomeBase = caminho.stem
        saida = Path(f"../Datasets/{nomeBase}_disciplinas.txt")

        print(f"\n[INFO] Processando: {caminho.name}")

        # Reinicializa os dicionários para cada histórico
        cco = deepcopy(cco_padrao)
        sin = deepcopy(sin_padrao)

        try:
            with fitz.open(caminho) as doc:
                texto = "\n".join([page.get_text() for page in doc])

            disciplinas = parserDisciplina(texto)
            salvaResultado(disciplinas, saida)

            if "CCO" in nomeBase.upper():
                dicionario = atualizar_situacoes(str(saida), cco)
            else:
                dicionario = atualizar_situacoes(str(saida), sin)

            viaveis = disciplinas_viaveis(dicionario)
            pontuadas = pontuar_disciplinas_viaveis(dicionario, viaveis)

            print("\n🎯 Pontuação das Disciplinas Viáveis:")
            for d in sorted(pontuadas, key=lambda x: -x["pontuacao"]):
                print(f'{d["codigo"]} - {d["nome"]} | Pontuação: {d["pontuacao"]}')

            resultado = calcular_limite_ch_aprovada(str(saida))

            print("\n📊 Limite recomendado de CH para matrícula:")
            print("• Limite total:", resultado["limite_final"], "horas")
            print("• Aproveitamento:", resultado["percentual_aproveitamento"], "%")
            print("• CH total cursada nos últimos 2 períodos:", resultado["ch_total"])
            print("• CH aprovada:", resultado["ch_aprovada"])
            print("• Períodos analisados:", ", ".join(resultado["periodos_analisados"]))

            candidatas = [dados["codigo"] for dados in dicionario.values()
              if dados["situacao"] != 1 and dados["parametro"] > 0]

            selecionadas, pontuacao = funcao_objetivo(dicionario, candidatas, resultado["limite_final"])

            print("\n✅ Sugestão final de matrícula:")
            for codigo in selecionadas:
                dados = next(v for v in dicionario.values() if v["codigo"] == codigo)
                print(f"- {codigo} - {dados['nome']} (CH: {dados['ch']} | Pontuação: {dados['parametro']})")

            print("📈 Pontuação total obtida:", pontuacao)
            
        except Exception as e:
            print(f"[ERRO] Falha ao processar {caminho.name}: {e}")