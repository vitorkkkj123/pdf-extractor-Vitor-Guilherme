import argparse
from pypdf import PdfReader
import os

def extrair(caminho, paginas=None):
    try:
        if not os.path.exists(caminho):
            return None, "Erro: Arquivo PDF não encontrado!"
        
        leitor = PdfReader(caminho)
        texto = ""
        indices = paginas if paginas else range(len(leitor.pages))
        
        for i in indices:
            if 0 <= i < len(leitor.pages):
                texto += f"\n--- PÁGINA {i+1} ---\n"
                texto += leitor.pages[i].extract_text()
        
        return texto, None
    except Exception as e:
        return None, f"Erro técnico: {e}"

if __name__ == "__main__":
    print("--- 📄 EXTRATOR DE PDF INTERATIVO ---")
    
    # Pegando o caminho do arquivo de forma mais amigável
    caminho_input = input("Digite o caminho do arquivo PDF (ex: documento.pdf): ")
    
    # Pergunta opcional sobre as páginas
    opcao_paginas = input("Deseja extrair páginas específicas? (Ex: 1-3 ou 1,3) [Deixe em branco para TUDO]: ")
    
    pags_selecionadas = None
    if opcao_paginas.strip():
        try:
            if "-" in opcao_paginas:
                ini, fim = map(int, opcao_paginas.split("-"))
                pags_selecionadas = list(range(ini-1, fim))
            else:
                pags_selecionadas = [int(p)-1 for p in opcao_paginas.split(",")]
        except:
            print("⚠️ Formato de páginas inválido. Extraindo tudo por padrão...")

    # Executa a extração
    resultado, erro = extrair(caminho_input, pags_selecionadas)

    if erro:
        print(f"❌ {erro}")
    else:
        # SALVANDO EM TXT
        nome_saida = input("Digite o nome do arquivo para salvar (ex: resultado.txt): ")
        if not nome_saida.endswith(".txt"):
            nome_saida += ".txt"
            
        with open(nome_saida, "w", encoding="utf-8") as f:
            f.write(resultado)
        
        print(f"✅ Sucesso! O texto foi salvo em: {nome_saida}")