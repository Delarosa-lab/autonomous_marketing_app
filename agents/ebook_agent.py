import os
from fpdf import FPDF

# Pasta de saída dos ebooks
EBOOK_OUTPUT = "output/ebooks"
os.makedirs(EBOOK_OUTPUT, exist_ok=True)

def criar_ebook(titulo, texto, nome_arquivo):
    """
    Cria um ebook PDF com título e conteúdo fornecido.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, titulo, align='C')
    pdf.ln(10)
    
    # Conteúdo
    pdf.set_font("Arial", '', 12)
    for linha in texto.split("\n"):
        pdf.multi_cell(0, 10, linha)
    
    caminho_ebook = os.path.join(EBOOK_OUTPUT, nome_arquivo)
    pdf.output(caminho_ebook)
    print(f"Ebook salvo: {caminho_ebook}")
    return caminho_ebook

def gerar_ebook_semanal(texto_semanal, textos_diarios):
    """
    Gera 1 ebook semanal (do vídeo longo) e 5 ebooks diários (opcional, dos vídeos curtos)
    """
    # Ebook do vídeo longo semanal
    criar_ebook("Ebook Semanal", texto_semanal, "ebook_semanal.pdf")
    
    # Ebooks dos vídeos curtos (opcional)
    for i, texto in enumerate(textos_diarios, start=1):
        criar_ebook(f"Ebook Curto Dia {i}", texto, f"ebook_curto_dia_{i}.pdf")

if __name__ == "__main__":
    # Exemplo de uso
    texto_longo = "Este é o roteiro do vídeo longo semanal. Pode conter várias linhas.\nExemplo de conteúdo."
    textos_curtos = [
        "Roteiro do vídeo curto dia 1",
        "Roteiro do vídeo curto dia 2",
        "Roteiro do vídeo curto dia 3",
        "Roteiro do vídeo curto dia 4",
        "Roteiro do vídeo curto dia 5",
    ]
    gerar_ebook_semanal(texto_longo, textos_curtos)
