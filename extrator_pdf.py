import PyPDF2
import re

def extrair_texto_pdf(caminho_arquivo):
    with open(caminho_arquivo, "rb") as arquivo:
        leitor_pdf = PyPDF2.PdfReader(arquivo)
        texto = ""
        for pagina in leitor_pdf.pages:
            texto += pagina.extract_text()
    return texto

def extrair_cnpj(texto):
    m = re.search(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b", texto)
    if m:
        cnpj_formatado = m.group(0)
    return cnpj_formatado

def extrair_razao_social(texto):
    m = re.search(r"NOME EMPRESARIAL\s+([A-Z0-9 .!'\-–&]+)", texto)
    if m:
        razao_social = m.group(1).strip()
    return razao_social

def extrair_cep(texto):
    texto = texto.replace("BAIRRO", " BAIRRO")
    m = re.search(r"\b\d{2}\.\d{3}-\d{3}\b", texto)
    if not m:
        return None
    cep = m.group(0).replace(".", "")
    return cep

def extrair_numero_logradouro(texto):
    m = re.search(r"N[ÚU]MERO\s+(\d+)", texto)
    if m:
        numero = m.group(1)
    return numero

def extrair_complemento_logradouro(texto):
    m = re.search(r"COMPLEMENT\s*O\s+([A-Z0-9 .\-–]+)", texto)
    if m:
        complemento = m.group(1).strip()
    return complemento

def extrair_email(texto):
    texto = texto.replace("TELEFONE", " TELEFONE")
    m = re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", texto, re.I)
    if m:
        email = m.group(0).lower()
    return email

def extrair_telefone(texto):
    m = re.search(r"\(\d{2}\)\s*\d{4,5}-\d{4}", texto)
    if m:
        telefone = m.group(0)
    return telefone