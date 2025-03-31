from pathlib import Path
import fitz
from parser import parserDisciplina, salvaResultado
from data import historicos

if __name__ == "__main__":
    for dataset in historicos:
        caminho = Path('../Datasets/'+ dataset)
        nomeBase = caminho.stem 
        saida = Path(f"../Datasets/{nomeBase}_disciplinas.txt")

        print(f"[INFO] Processando: {caminho}")

        try:
            with fitz.open(caminho) as doc:
                texto = "\n".join([page.get_text() for page in doc])

            disciplinas = parserDisciplina(texto)
            salvaResultado(disciplinas, saida)

        except Exception as e:
            print(f"[ERRO] Falha ao processar {caminho}: {e}")
