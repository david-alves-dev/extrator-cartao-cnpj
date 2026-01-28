import PyPDF2
import re

class ExtratorCartaoCnpj():
    
    def __init__(self, caminho_arquivo): 
        self.caminho_arquivo = caminho_arquivo
        self.texto_pdf = ''

        self.cnpj = None
        self.razao_social = None
        self.cep = None
        self.numero_logradouro = None
        self.complemento_logradouro = None
        self.email = None
        self.telefone = None

    def carregar_texto_pdf(self): 
        with open(self.caminho_arquivo, "rb") as arquivo:
            leitor_pdf = PyPDF2.PdfReader(arquivo)
            partes = []
            for pagina in leitor_pdf.pages:
                partes.append(pagina.extract_text() or "")
        self.texto_pdf = "\n".join(partes)
        return self.texto_pdf
    
    def extrair_cnpj(self):
        m = re.search(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b", self.texto_pdf)
        if not m:
            self.cnpj = None
            return None
        self.cnpj_formatado = m.group(0)
        return self.cnpj
    
    def extrair_razao_social(self):
        m = re.search(r"NOME EMPRESARIAL\s+([A-Z0-9 .!'\-–&]+)", self.texto_pdf)
        if not m:
            self.razao_social = None
            return None
        self.razao_social = m.group(1).strip()
        return self.razao_social

    def extrair_cep(self):
        texto_cep = self.texto_pdf.replace("BAIRRO", " BAIRRO")
        m = re.search(r"\b\d{2}\.\d{3}-\d{3}\b", texto_cep)
        if not m:
            self.cep = None
            return None
        self.cep = m.group(0).replace(".", "")
        return self.cep

    def extrair_numero_logradouro(self):
        m = re.search(r"N[ÚU]MERO\s+(\d+)", self.texto_pdf)
        if not m:
            self.numero = None
            return None    
        self.numero = m.group(1)
        return self.numero

    def extrair_complemento_logradouro(self):
        m = re.search(r"COMPLEMENT\s*O\s+([A-Z0-9 .\-–]+)", self.texto_pdf)
        if not m:
            self.complemento = None
            return None
        self.complemento = m.group(1).strip()
        return self.complemento

    def extrair_email(self):
        texto_email = self.texto_pdf.replace("TELEFONE", " TELEFONE")
        m = re.search(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", texto_email, re.I)
        if not m:
            self.email = None
            return None
        self.email = m.group(0).lower()
        return self.email

    def extrair_telefone(self):
        m = re.search(r"\(\d{2}\)\s*\d{4,5}-\d{4}", self.texto_pdf)
        if not m:
            self.telefone = None
            return None
        self.telefone = m.group(0)
        return self.telefone
    
    def extrair_tudo(self):
        return {
            "cnpj": self.extrair_cnpj(),
            "razao_social": self.extrair_razao_social(),
            "cep": self.extrair_cep(),
            "numero": self.extrair_numero_logradouro(),
            "complemento": self.extrair_complemento_logradouro(),
            "email": self.extrair_email(),
            "telefone": self.extrair_telefone(),
        }
