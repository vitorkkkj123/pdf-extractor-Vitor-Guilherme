# 📄 Extrator de PDF - Vitor Guilherme

Este projeto é uma ferramenta de linha de comando desenvolvida para extrair texto de arquivos PDF de forma simples e eficiente. Projeto desenvolvido para a disciplina de [Nome da Disciplina].

## 🚀 Funcionalidades

* **Extração Completa:** Lê todo o conteúdo de um arquivo PDF de uma só vez.
* **Extração por Páginas:** Permite selecionar páginas específicas (ex: 1,3,5) ou intervalos (ex: 1-3).
* **Versionamento Profissional:** Desenvolvido utilizando o fluxo de branches e Pull Requests no GitHub.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **PyPDF:** Biblioteca para manipulação de arquivos PDF.
* **Argparse:** Para criação da interface de linha de comando.

## 📦 Como Instalar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/vitorkkkj123/extrator-pdf-Vitor-Guilherme.git](https://github.com/vitorkkkj123/extrator-pdf-Vitor-Guilherme.git)

2. Instale as dependências:

pip install pypdf

💻 Como Usar
1. Extração de todo o texto:

python src/extrator.py --input seu_arquivo.pdf

2. Extração de páginas específicas:

python src/extrator.py --input seu_arquivo.pdf --pages 1,3

3. Extração de um intervalo de páginas:

python src/extrator.py --input seu_arquivo.pdf --pages 1-5

Desenvolvido por Vitor Guilherme