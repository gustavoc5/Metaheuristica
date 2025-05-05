from pathlib import Path
from parser import parserDisciplina, salvaResultado
from data import historicos
from copy import deepcopy
import fitz
import time
import random
import math
from collections import defaultdict
from data import cco as cco_padrao, sin as sin_padrao


def disciplinas_viaveis(dicionario_principal, dicionario_equivalente):
    viaveis = []
    for id_disc, dados in dicionario_principal.items():
        if dados["situacao"] == 1:
            continue
        requisitos = dados["requisito"]
        if requisitos == 0 or requisitos == [] or all(
            isinstance(req_id, str) and dicionario_principal.get(req_id, {}).get("situacao") == 1
            for req_id in requisitos
        ):
            if dados.get("horario"):
                viaveis.append(f'{dados["codigo"]} - {dados["nome"]}')
            else:
                for cod_equiv in dados.get("equivalentes", []):
                    for eq in dicionario_equivalente.values():
                        if eq["codigo"] == cod_equiv and eq.get("horario") and eq.get("situacao") != 1:
                            dados["horario"] = eq["horario"]
                            viaveis.append(f'{dados["codigo"]} - {dados["nome"]} (ofertada como {cod_equiv})')
                            break
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


def horarios_conflitantes(horarios1, horarios2):
    return any(h1 == h2 for h1 in horarios1 for h2 in horarios2)


def heuristica_aleatoria(dicionario, candidatas, limite_ch):
    disciplinas_info = [
        {
            "id": id_disc,
            "codigo": dados["codigo"],
            "nome": dados["nome"],
            "ch": int(dados["ch"]),
            "parametro": dados.get("parametro", 0),
            "horario": dados.get("horario")
        }
        for id_disc, dados in dicionario.items()
        if dados["codigo"] in candidatas and dados.get("horario")
    ]
    random.shuffle(disciplinas_info)
    ch_total = 0
    selecionadas = []
    horarios_ocupados = []
    for disc in disciplinas_info:
        if any(horarios_conflitantes(disc["horario"], h["horario"]) for h in horarios_ocupados):
            continue
        if ch_total + disc["ch"] <= limite_ch:
            selecionadas.append(disc["codigo"])
            ch_total += disc["ch"]
            horarios_ocupados.append(disc)
    return selecionadas


def funcao_objetivo(dicionario, candidatas, limite_ch):
    disciplinas_info = [
        {
            "id": id_disc,
            "codigo": dados["codigo"],
            "nome": dados["nome"],
            "ch": int(dados["ch"]),
            "parametro": dados["parametro"],
            "horario": dados["horario"]
        }
        for id_disc, dados in dicionario.items()
        if dados["codigo"] in candidatas and dados.get("horario")
    ]
    disciplinas_info.sort(key=lambda d: d["parametro"], reverse=True)
    ch_total = 0
    pontuacao_total = 0
    selecionadas = []
    horarios_ocupados = []
    for disc in disciplinas_info:
        if any(horarios_conflitantes(disc["horario"], h["horario"]) for h in horarios_ocupados):
            continue
        if ch_total + disc["ch"] <= limite_ch:
            selecionadas.append(disc["codigo"])
            pontuacao_total += disc["parametro"]
            ch_total += disc["ch"]
            horarios_ocupados.append(disc)
    return selecionadas, pontuacao_total


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
        dicionario[id_disc]["parametro"] = nota
        resultados.append({"codigo": dados["codigo"], "nome": dados["nome"], "pontuacao": nota})
    return resultados

def simulated_annealing(dicionario, candidatas, limite_ch, max_iter=1000, temp_inicial=100.0, temp_final=1.0, alpha=0.95):
    def gerar_vizinho(solucao):
        vizinho = solucao.copy()
        tentativas = 0
        while True:
            tentativas += 1
            if tentativas > 100:
                return vizinho  # evita loop infinito

            remover = random.choice(vizinho)
            codigo_remover = remover["codigo"]
            candidatos_restantes = [d for d in disciplinas_info if d["codigo"] not in [s["codigo"] for s in vizinho]]

            if not candidatos_restantes:
                continue

            adicionar = random.choice(candidatos_restantes)
            nova_solucao = [s for s in vizinho if s["codigo"] != codigo_remover]
            nova_solucao.append(adicionar)

            if not tem_conflito(nova_solucao) and soma_ch(nova_solucao) <= limite_ch:
                return nova_solucao

    def soma_ch(solucao):
        return sum(int(d["ch"]) for d in solucao)

    def tem_conflito(solucao):
        for i in range(len(solucao)):
            for j in range(i + 1, len(solucao)):
                if horarios_conflitantes(solucao[i]["horario"], solucao[j]["horario"]):
                    return True
        return False

    def pontuacao_total(solucao):
        return sum(d["parametro"] for d in solucao)

    # Cria lista de disciplinas candidatas com horários
    disciplinas_info = []
    for id_disc, dados in dicionario.items():
        if dados["codigo"] in candidatas and dados.get("horario"):
            disciplinas_info.append({
                "id": id_disc,
                "codigo": dados["codigo"],
                "nome": dados["nome"],
                "ch": int(dados["ch"]),
                "parametro": dados["parametro"],
                "horario": dados["horario"]
            })

    disciplinas_info.sort(key=lambda d: d["parametro"], reverse=True)

    # Solução inicial gulosa (a mesma da função_objetivo)
    solucao_atual = []
    ch_total = 0
    for disc in disciplinas_info:
        if not any(horarios_conflitantes(disc["horario"], s["horario"]) for s in solucao_atual) and ch_total + disc["ch"] <= limite_ch:
            solucao_atual.append(disc)
            ch_total += disc["ch"]

    melhor_solucao = solucao_atual.copy()
    melhor_pontuacao = pontuacao_total(melhor_solucao)

    temperatura = temp_inicial
    iteracao = 0

    while temperatura > temp_final and iteracao < max_iter:
        vizinho = gerar_vizinho(solucao_atual)
        delta = pontuacao_total(vizinho) - pontuacao_total(solucao_atual)

        if delta > 0 or random.random() < math.exp(delta / temperatura):
            solucao_atual = vizinho
            if pontuacao_total(solucao_atual) > melhor_pontuacao:
                melhor_solucao = solucao_atual.copy()
                melhor_pontuacao = pontuacao_total(solucao_atual)

        temperatura *= alpha
        iteracao += 1

    return melhor_solucao, melhor_pontuacao

if __name__ == "__main__":
    for dataset in historicos:
        caminho = Path(f'../Datasets/{dataset}')
        nomeBase = caminho.stem
        saida = Path(f"../Datasets/{nomeBase}_disciplinas.txt")
        print(f"\n[INFO] Processando: {caminho.name}")

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

            d_eq = sin if "CCO" in nomeBase.upper() else cco

            viaveis = disciplinas_viaveis(dicionario, d_eq)
            pontuar_disciplinas_viaveis(dicionario, viaveis)

            resultado = calcular_limite_ch_aprovada(str(saida))
            limite = resultado["limite_final"]

            print("\n📊 Limite recomendado de CH para matrícula:")
            print("• Limite total:", limite, "horas")
            print("• Aproveitamento:", resultado["percentual_aproveitamento"], "%")
            print("• CH total cursada nos últimos 2 períodos:", resultado["ch_total"])
            print("• CH aprovada:", resultado["ch_aprovada"])
            print("• Períodos analisados:", ", ".join(resultado["periodos_analisados"]))

            candidatas = [dados["codigo"] for dados in dicionario.values() if dados["situacao"] != 1 and dados.get("parametro", 0) > 0]

            # GULOSA
            print("\n✅ Heurística Gulosa:")
            inicio = time.time()
            selecionadas_gulosa, pontuacao_gulosa = funcao_objetivo(dicionario, candidatas, limite)
            fim = time.time()
            for codigo in selecionadas_gulosa:
                dados = next(v for v in dicionario.values() if v["codigo"] == codigo)
                print(f"- {codigo} - {dados['nome']} (CH: {dados['ch']} | Pontuação: {dados['parametro']})")
            print("Pontuação total:", pontuacao_gulosa, "| Tempo:", round(fim - inicio, 4), "s")

            # ALEATÓRIA
            print("\n✅ Heurística Aleatória:")
            inicio = time.time()
            selecionadas_aleatoria = heuristica_aleatoria(dicionario, candidatas, limite)
            fim = time.time()
            for codigo in selecionadas_aleatoria:
                dados = next(v for v in dicionario.values() if v["codigo"] == codigo)
                print(f"- {codigo} - {dados['nome']} (CH: {dados['ch']} | Pontuação: {dados.get('parametro', 0)})")
            pont_aleatoria = sum(dados.get("parametro", 0) for dados in dicionario.values() if dados["codigo"] in selecionadas_aleatoria)
            print("Pontuação total:", pont_aleatoria, "| Tempo:", round(fim - inicio, 4), "s")

            # HÍBRIDA (Simulated Annealing)
            print("\n✅ Heurística Híbrida (Simulated Annealing):")
            inicio = time.time()
            solucao_refinada, pontuacao_refinada = simulated_annealing(dicionario, candidatas, limite)
            fim = time.time()
            for d in solucao_refinada:
                print(f"- {d['codigo']} - {d['nome']} (CH: {d['ch']} | Pontuação: {d['parametro']})")
            print("Pontuação total:", pontuacao_refinada, "| Tempo:", round(fim - inicio, 4), "s")

        except Exception as e:
            print(f"[ERRO] Falha ao processar {caminho.name}: {e}")
        finally:
            print(f"[INFO] Processamento de {caminho.name} concluído.\n")
