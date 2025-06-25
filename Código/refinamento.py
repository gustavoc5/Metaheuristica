from pathlib import Path
from parser import parserDisciplina, salvaResultado
from data import historicos
import numpy as np
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import statistics
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
            all(isinstance(req_id, str) for req_id in requisitos) and dicionario_principal.get(req_id, {}).get("situacao") == 1
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
                try:
                    ch = int(ch_str)
                except ValueError:
                    print(f"[WARNING] Invalid CH value encountered: '{ch_str}'")
                    continue
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
    def gerar_vizinho(sol):
        for _ in range(100):
            novo = sol.copy()

            if random.random() < 0.5:                 # troca dupla
                out1, out2 = random.sample(novo, 2)
                cand = [d for d in disciplinas_info if d["codigo"]
                        not in {s["codigo"] for s in novo}]
                if len(cand) < 2: continue
                in1, in2 = random.sample(cand, 2)
                novo.remove(out1); novo.remove(out2)
                novo += [in1, in2]

            else:                                     # remove-e-adiciona
                out = random.choice(novo)
                cand = [d for d in disciplinas_info if d["codigo"]
                        not in {s["codigo"] for s in novo}]
                if not cand: continue
                inp = random.choice(cand)
                novo.remove(out); novo.append(inp)

            if not tem_conflito(novo) and soma_ch(novo) <= limite_ch:
                return novo
        return sol      # fallback

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

    # Solução inicial aleatória
    random.shuffle(disciplinas_info)
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

def heuristica_abc(dicionario, candidatas, limite_ch, num_abelhas=20, num_iter=50, limite_tentativas=5):
    def avaliar(solucao):
        ch_total = sum(d["ch"] for d in solucao)
        if ch_total > limite_ch:
            return 0
        if conflitos_horarios(solucao):
            return 0
        return sum(d["parametro"] for d in solucao)

    def conflitos_horarios(solucao):
        for i in range(len(solucao)):
            for j in range(i + 1, len(solucao)):
                if horarios_conflitantes(solucao[i]["horario"], solucao[j]["horario"]):
                    return True
        return False

    disciplinas_info = [dados for dados in dicionario.values() if dados["codigo"] in candidatas and dados.get("horario")]
    melhores_solucoes = []
    tentativas = [0] * num_abelhas

    # Fase de abelhas empregadas: gera soluções iniciais aleatórias
    populacao = []
    for _ in range(num_abelhas):
        random.shuffle(disciplinas_info)
        solucao = []
        ch_total = 0
        for d in disciplinas_info:
            if ch_total + d["ch"] <= limite_ch and not conflitos_horarios(solucao + [d]):
                solucao.append(d)
                ch_total += d["ch"]
        populacao.append(solucao)
        melhores_solucoes.append((solucao, avaliar(solucao)))

    for _ in range(num_iter):
        # Fase das abelhas empregadas: Explora vizinhança
        for i in range(num_abelhas):
            vizinho = populacao[i][:]
            if vizinho:
                idx = random.randint(0, len(vizinho) - 1)
                nova_disc = random.choice(disciplinas_info)
                if nova_disc not in vizinho:
                    vizinho[idx] = nova_disc
            if avaliar(vizinho) > melhores_solucoes[i][1]:
                populacao[i] = vizinho
                melhores_solucoes[i] = (vizinho, avaliar(vizinho))
                tentativas[i] = 0
            else:
                tentativas[i] += 1

        # Fase das abelhas observadoras: Explora melhores soluções
        total_avaliacao = sum(s[1] for s in melhores_solucoes)
        probabilidades = [s[1] / total_avaliacao if total_avaliacao > 0 else 0 for s in melhores_solucoes]
        for _ in range(num_abelhas):
            i = random.choices(range(num_abelhas), weights=probabilidades)[0]
            vizinho = melhores_solucoes[i][0][:]
            if vizinho:
                idx = random.randint(0, len(vizinho) - 1)
                nova_disc = random.choice(disciplinas_info)
                if nova_disc not in vizinho:
                    vizinho[idx] = nova_disc
            if avaliar(vizinho) > melhores_solucoes[i][1]:
                melhores_solucoes[i] = (vizinho, avaliar(vizinho))
                tentativas[i] = 0

        # Fase das abelhas escoteiras: substitui soluções estagnadas
        for i in range(num_abelhas):
            if tentativas[i] >= limite_tentativas:
                random.shuffle(disciplinas_info)
                nova_solucao = []
                ch_total = 0
                for d in disciplinas_info:
                    if ch_total + d["ch"] <= limite_ch and not conflitos_horarios(nova_solucao + [d]):
                        nova_solucao.append(d)
                        ch_total += d["ch"]
                populacao[i] = nova_solucao
                melhores_solucoes[i] = (nova_solucao, avaliar(nova_solucao))
                tentativas[i] = 0

    melhor_solucao = max(melhores_solucoes, key=lambda s: s[1])[0]
    return [d["codigo"] for d in melhor_solucao]

def resumo(lst):
    return (min(lst), max(lst),
            round(statistics.mean(lst), 4),
            round(statistics.stdev(lst), 4) if len(lst) > 1 else 0)

def imprime(label, ponts, tempos):
    pmin, pmax, pmean, psd = resumo(ponts)
    tmin, tmax, tmean, tsd = resumo(tempos)
    print(f"\n🔸 {label:<9}"
          f"  Pontuação  min={pmin:4} máx={pmax:4} "
          f"média={pmean:6} σ={psd:6}"
          f" | Tempo  min={tmin:.4f}s máx={tmax:.4f}s "
          f"média={tmean:.4f}s σ={tsd:.4f}s")

# Nova heurística de refinamento (busca local)
def heuristica_refinamento(dicionario, candidatas, limite_ch, max_iter=500):
    import random, math
    
    # Monta a lista de disciplinas candidatas com todos os dados
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

    def soma_ch(sol):
        return sum(d["ch"] for d in sol)
    def tem_conflito(sol):
        for i in range(len(sol)):
            for j in range(i+1, len(sol)):
                # reusa sua função de conflito
                if horarios_conflitantes(sol[i]["horario"], sol[j]["horario"]):
                    return True
        return False
    def pontuacao(sol):
        return sum(d["parametro"] for d in sol)

    # **1) Solução inicial aleatória** (usa sua heurística aleatória)
    sel_codes = heuristica_aleatoria(dicionario, candidatas, limite_ch)
    solucao_atual = [d for d in disciplinas_info if d["codigo"] in sel_codes]
    pont_atual = pontuacao(solucao_atual)

    # mantém melhor solução encontrada
    melhor_sol = solucao_atual[:]
    melhor_pont = pont_atual

    # 2) Busca local: tenta k-swaps até max_iter
    for _ in range(max_iter):
        # pega um vizinho trocando 1 dentro por 1 fora
        vizinho = solucao_atual[:]
        out = random.choice(vizinho)
        candidatos_fora = [d for d in disciplinas_info if d["codigo"] not in {x["codigo"] for x in vizinho}]
        if not candidatos_fora:
            break
        inp = random.choice(candidatos_fora)
        vizinho.remove(out)
        vizinho.append(inp)

        # só aceita se for válido e melhorar
        if not tem_conflito(vizinho) and soma_ch(vizinho) <= limite_ch:
            pont_viz = pontuacao(vizinho)
            if pont_viz > pont_atual:
                solucao_atual = vizinho
                pont_atual = pont_viz
                if pont_viz > melhor_pont:
                    melhor_sol, melhor_pont = vizinho[:], pont_viz

    # retorna códigos + pontuação
    return [d["codigo"] for d in melhor_sol], melhor_pont

def main():
    random.seed()
    N_RODADAS      = 30

    selecionados   = [f"historico_CCO-{i}.pdf" for i in range(1,6)] + \
                     [f"historico_SIN-{i}.pdf" for i in range(1,6)]
    dataset_labels = [f"CCO{i}" for i in range(1,6)] + \
                     [f"SIN{i}" for i in range(1,6)]
    metodos        = ["Gulosa","Aleatória","SA","ABC"]

    # estrutura para acumular estatísticas e soluções
    stats      = {m:{"pont":[], "time":[]} for m in metodos}
    sols       = {m:[]             for m in metodos}
    resultados = []  # cada elemento vira uma linha na tabela final

    for dataset, label in zip(selecionados, dataset_labels):
        caminho = Path(f"../Datasets/{dataset}")
        nomeBase = caminho.stem

        # 1) pré-processamento
        with fitz.open(caminho) as doc:
            texto = "\n".join(p.get_text() for p in doc)
        saida = Path(f"../Datasets/{nomeBase}_disciplinas.txt")
        salvaResultado(parserDisciplina(texto), saida)

        base_main  = deepcopy(cco_padrao if "CCO" in nomeBase.upper() else sin_padrao)
        base_equiv = deepcopy(sin_padrao if "CCO" in nomeBase.upper() else cco_padrao)
        dicionario = atualizar_situacoes(str(saida), base_main)

        viaveis  = disciplinas_viaveis(dicionario, base_equiv)
        pontuar_disciplinas_viaveis(dicionario, viaveis)

        # 2) limite de CH com bounds de 192–416
        ch_calc = calcular_limite_ch_aprovada(str(saida))["limite_final"]
        limite  = min(max(ch_calc, 192), 416)

        candidatas = [d["codigo"] for d in dicionario.values() if d.get("parametro",0)>0]

        # limpa stats / sols da instância anterior
        for m in metodos:
            stats[m]["pont"].clear()
            stats[m]["time"].clear()
            sols[m].clear()

        # 3) rodadas de cada heurística
        for _ in range(N_RODADAS):
            # – Gulosa
            t0 = time.perf_counter()
            sol, _ = funcao_objetivo(dicionario, candidatas, limite)
            tempo = time.perf_counter() - t0
            p     = sum(d["parametro"] for d in dicionario.values() if d["codigo"] in sol)
            stats["Gulosa"]["pont"].append(p)
            stats["Gulosa"]["time"].append(tempo)
            sols["Gulosa"].append(sol)

            # – Aleatória
            t0 = time.perf_counter()
            sol = heuristica_aleatoria(dicionario, candidatas, limite)
            tempo = time.perf_counter() - t0
            p = sum(d["parametro"] for d in dicionario.values() if d["codigo"] in sol)
            stats["Aleatória"]["pont"].append(p)
            stats["Aleatória"]["time"].append(tempo)
            sols["Aleatória"].append(sol)

            # – SA
            t0 = time.perf_counter()
            sol_sa, p_sa = simulated_annealing(dicionario, candidatas, limite)
            tempo = time.perf_counter() - t0
            stats["SA"]["pont"].append(p_sa)
            stats["SA"]["time"].append(tempo)
            sols["SA"].append([d["codigo"] for d in sol_sa])

            # – ABC
            t0 = time.perf_counter()
            sol_abc = heuristica_abc(dicionario, candidatas, limite)
            tempo = time.perf_counter() - t0
            p = sum(d["parametro"] for d in dicionario.values() if d["codigo"] in sol_abc)
            stats["ABC"]["pont"].append(p)
            stats["ABC"]["time"].append(tempo)
            sols["ABC"].append(sol_abc)

        # 4) agregação dos resultados por método
        for m in metodos:
            ponts  = stats[m]["pont"]
            tempos = stats[m]["time"]
            idx_best = ponts.index(max(ponts))
            resultados.append({
                "Instância":    label,
                "Heurística":   m,
                "Min":          min(ponts),
                "Máx":          max(ponts),
                "Desvio":       round(statistics.stdev(ponts),4) if len(ponts)>1 else 0,
                "Tempo Médio":  round(statistics.mean(tempos),4),
                "Solução Ótima": ",".join(sols[m][idx_best])
            })

    # 5) montar DataFrame e salvar CSV
    df = pd.DataFrame(resultados)
    df.to_csv("resultados_heuristicas.csv", index=False)
    print(df.to_markdown(index=False))

    # 6) gerar gráfico de barras das pontuações máximas
    max_gulosa = [df[(df["Instância"]==inst)&(df["Heurística"]=="Gulosa")]["Máx"].iloc[0]
                  for inst in dataset_labels]
    max_alea   = [df[(df["Instância"]==inst)&(df["Heurística"]=="Aleatória")]["Máx"].iloc[0]
                  for inst in dataset_labels]
    max_sa     = [df[(df["Instância"]==inst)&(df["Heurística"]=="SA")]["Máx"].iloc[0]
                  for inst in dataset_labels]
    max_abc    = [df[(df["Instância"]==inst)&(df["Heurística"]=="ABC")]["Máx"].iloc[0]
                  for inst in dataset_labels]

    x = np.arange(len(dataset_labels))
    w = 0.2

    plt.figure(figsize=(12, 6))
    plt.bar( x - 1.5*w, max_gulosa, width=w, label="Gulosa")
    plt.bar( x - 0.5*w, max_alea,   width=w, label="Aleatória")
    plt.bar( x + 0.5*w, max_sa,     width=w, label="SA")
    plt.bar( x + 1.5*w, max_abc,    width=w, label="ABC")

    plt.xlabel("Instância")
    plt.ylabel("Pontuação máxima (30 exec.)")
    plt.title("Comparação de Heurísticas — 10 Instâncias (CCO1–CCO5, SIN1–SIN5)")
    plt.xticks(x, dataset_labels, rotation=20, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafico_comparativo_heuristicas.png", dpi=300)
    plt.show()



if __name__ == "__main__":
    from copy import deepcopy
    import statistics
    main()