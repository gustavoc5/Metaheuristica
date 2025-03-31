from pathlib import Path
import fitz
from parser import parserDisciplina, salvaResultado
from data import historicos

if __name__ == "__main__":
    for arquivo_pdf in historicos:
        pdf_path = Path('../Datasets/'+ arquivo_pdf)
        nome_base = pdf_path.stem 
        saida = Path(f"../Datasets/{nome_base}_disciplinas.txt")

        print(f"[INFO] Processando: {pdf_path}")

        try:
            with fitz.open(pdf_path) as doc:
                texto = "\n".join([page.get_text() for page in doc])

            disciplinas = parserDisciplina(texto)
            salvaResultado(disciplinas, saida)

        except Exception as e:
            print(f"[ERRO] Falha ao processar {pdf_path}: {e}")
