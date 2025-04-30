import re
from pathlib import Path

# Carregar os dados existentes de data.py
from data import cco, sin, historicos, semana, horarios
from salvar import salvar_dicionario_em_data


def parse_horario_bruto(texto):
    horarios = []
    matches = re.findall(r'\((\d)(?:,(\d)|\((\d),(\d)\))\)', texto)
    for dia, h1, h2a, h2b in matches:
        dia = int(dia)
        if h1:
            horarios.append((dia, int(h1)))
        elif h2a and h2b:
            horarios.append((dia, int(h2a)))
            horarios.append((dia, int(h2b)))
    return horarios

def atualizar_horarios_cco_e_sin(caminho_txt="MateriasCCO_2024.2.txt"):
    with open(caminho_txt, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    codigos_cco = {dados["codigo"]: id_ for id_, dados in cco.items()}
    codigos_sin = {dados["codigo"]: id_ for id_, dados in sin.items()}

    atualizados_cco = 0
    atualizados_sin = 0

    for linha in linhas:
        partes = linha.strip().split("|")
        if len(partes) < 4:
            continue
        codigo = partes[1].strip()
        horario_bruto = partes[3].strip()
        horarios = parse_horario_bruto(horario_bruto)

        if codigo in codigos_cco:
            cco[codigos_cco[codigo]]["horario"] = horarios
            atualizados_cco += 1

        if codigo in codigos_sin:
            sin[codigos_sin[codigo]]["horario"] = horarios
            atualizados_sin += 1

    salvar_dicionario_em_data(cco, sin, historicos, semana, horarios)
    return atualizados_cco, atualizados_sin

# Executar atualização
atualizar_horarios_cco_e_sin()