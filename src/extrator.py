# Versão 1.0

from pypdf import PdfReader
import os

def extrair_texto_simples(caminho_pdf):
    """Lê todas as páginas de um PDF e retorna o texto extraído."""
    try:
        if not os.path.exists(caminho_pdf):
            return "Erro: Arquivo não encontrado."
            
        leitor = PdfReader(caminho_pdf)
        texto_completo = ""
        
        for pagina in leitor.pages:
            texto_completo += pagina.extract_text() + "\n"
            
        return texto_completo
    except Exception as e:
        return f"Erro ao ler PDF: {e}"

if __name__ == "__main__":
    # Teste rápido: se você tiver um arquivo chamado 'teste.pdf', ele vai ler.
    # Caso contrário, apenas imprimirá a mensagem de erro.
    arquivo = "teste.pdf"
    print(extrair_texto_simples(arquivo))