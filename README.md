# extrator-cartao-cnpj

<div align="left">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Acessar Site](https://img.shields.io/badge/Acessar%20Site-00A846?style=for-the-badge&logo=robotframework&logoColor=white)](https://davidalves.dev/)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/davidalves.dev)

</div>

Extrator de dados do Cartão CNPJ em PDF usando Python.

## ✨ Funcionalidades
- Lê um arquivo PDF do Cartão CNPJ.
- Extrai texto de todas as páginas.
- Localiza e retorna campos como:
  - CNPJ
  - Razão social
  - CEP
  - Número do logradouro
  - Complemento do logradouro
  - E-mail
  - Telefone

## ✅ Requisitos
- Python 3.8+
- PyPDF2

Instale a dependência:
```bash
pip install PyPDF2
```

## 🚀 Como usar
Exemplo básico de uso da classe:

```python
from extrator_cartao_cnpj import ExtratorCartaoCnpj

extrator = ExtratorCartaoCnpj("caminho/para/cartao_cnpj.pdf")
texto = extrator.texto_pdf

cnpj = extrator.cnpj(texto)
razao = extrator.razao_social(texto)
cep = extrator.cep(texto)
numero = extrator.numero_logradouro(texto)
complemento = extrator.complemento_logradouro(texto)
email = extrator.email(texto)
telefone = extrator.telefone(texto)
```

## ⚠️ Observações importantes
- Os métodos fazem `re.search` no texto do PDF. Se o padrão não for encontrado, retornam `None`.
- O padrão de texto do Cartão CNPJ costuma vir em caixa alta. Se o PDF tiver formatação diferente, os regex podem não encontrar os campos.
- O método `__init__` extrai todo o texto do PDF e armazena em `self.texto_pdf`.

## 🗂️ Estrutura do projeto
```
.
├── extrator_cartao_cnpj.py
└── README.md
```
