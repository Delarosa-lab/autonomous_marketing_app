from video_agent import gerar_conteudo_semanal
from ebook_agent import gerar_ebook_semanal

# Exemplo de textos do vídeo longo e curtos
texto_longo = """
Bem-vindo ao vídeo semanal! Este conteúdo é preparado automaticamente pelo agente.
Aqui você encontra dicas, tutoriais e informações importantes sobre marketing digital.
Você pode expandir este roteiro com qualquer conteúdo que desejar.
"""

textos_curtos = [
    "Dica rápida do dia 1 sobre marketing digital.",
    "Dica rápida do dia 2 sobre vendas online.",
    "Dica rápida do dia 3 sobre criação de conteúdo.",
    "Dica rápida do dia 4 sobre engajamento nas redes sociais.",
    "Dica rápida do dia 5 sobre produtos digitais."
]

def gerar_conteudo_completo():
    """
    Gera todo o conteúdo da semana:
    - Vídeo longo semanal
    - 5 vídeos curtos diários
    - Ebook do vídeo longo
    - Ebooks dos vídeos curtos
    """
    print("Gerando vídeos...")
    gerar_conteudo_semanal(texto_longo, textos_curtos)
    
    print("Gerando ebooks...")
    gerar_ebook_semanal(texto_longo, textos_curtos)
    
    print("Conteúdo completo gerado! Todos os arquivos estão na pasta output para aprovação humana.")

if __name__ == "__main__":
    gerar_conteudo_completo()
