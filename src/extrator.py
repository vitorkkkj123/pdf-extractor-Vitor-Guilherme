import argparse
from pypdf import PdfReader
import os

def extrair(caminho, paginas=None):
    try:
        if not os.path.exists(caminho):
            return "Erro: Arquivo não encontrado!"
        leitor = PdfReader(caminho)
        texto = ""
        # Se não houver páginas, lê todas. Se houver, ajusta para 0-indexed.
        indices = paginas if paginas else range(len(leitor.pages))
        for i in indices:
            if 0 <= i < len(leitor.pages):
                texto += f"\n--- PÁGINA {i+1} ---\n"
                texto += leitor.pages[i].extract_text()
        return texto
    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--pages", help="Ex: 1-3 ou 1,2")
    args = parser.parse_args()

    pags = None
    if args.pages:
        if "-" in args.pages:
            ini, fim = map(int, args.pages.split("-"))
            pags = list(range(ini-1, fim))
        else:
            pags = [int(p)-1 for p in args.pages.split(",")]

    print(extrair(args.input, pags))