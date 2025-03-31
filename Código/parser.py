from pathlib import Path
import fitz

def parserDisciplina(texto):
    linhas = texto.splitlines()
    disciplinas = []
    i = 0
    ano = None

    while i < len(linhas):
        linha = linhas[i].strip()

        if linha.count(".") == 1 and linha.replace(".", "").isdigit():
            ano = linha
            i += 1
            continue

        if i + 7 < len(linhas):
            nome = linhas[i].strip()
            situacao = linhas[i + 2].strip()
            codigo = linhas[i + 3].strip()
            ch = linhas[i + 4].strip()
            freq = linhas[i + 5].strip().replace(",", ".")
            nota = linhas[i + 6].strip().replace(",", ".")

            if codigo and codigo.isalnum() and situacao in ['APR', 'REPF', 'REPNF', 'TRANC', 'MATR', 'CUMP', 'DISP', 'REP']:
                disciplinas.append({
                    "ano": ano,
                    "codigo": codigo,
                    "nome": nome,
                    "ch": int(ch) if ch.isdigit() else 0,
                    "frequencia": float(freq) if freq.replace('.', '', 1).isdigit() else 0.0,
                    "nota": nota if nota != '--' else "N/A",
                    "situacao": situacao
                })
                i += 8 
            else:
                i += 1
        else:
            i += 1

    return disciplinas


def salvaResultado(lista, caminho_saida):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        for d in lista:
            f.write(
                f"{d['ano']} | {d['codigo']} | {d['nome']} | CH: {d['ch']} | Freq: {d['frequencia']}% | "
                f"Nota: {d['nota']} | Situação: {d['situacao']}\n"
            )
    print(f"[OK] Arquivo salvo em: {caminho_saida}")


if __name__ == "__main__":
    pdf_path = Path("../Datasets/historico_CCO-4.pdf")
    output_txt = Path("disciplinas_extraidas.txt")

    with fitz.open(pdf_path) as doc:
        texto = "\n".join([page.get_text() for page in doc])

    disciplinas = parserDisciplina(texto)
    salvaResultado(disciplinas, output_txt)
