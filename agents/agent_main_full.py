from video_agent import gerar_conteudo_semanal
from ebook_agent import gerar_ebook_semanal
from social_agent import mostrar_postagens_para_aprovacao, aprovar_postagem
from marketing_agent import registrar_venda, aprovar_marketing, gerar_relatorio

# Textos de exemplo
texto_longo = """
Bem-vindo ao vídeo semanal! Este conteúdo é preparado automaticamente pelo agente.
Aqui você encontra dicas, tutoriais e informações importantes sobre marketing digital.
"""

textos_curtos = [
    "Dica rápida do dia 1 sobre marketing digital.",
    "Dica rápida do dia 2 sobre vendas online.",
    "Dica rápida do dia 3 sobre criação de conteúdo.",
    "Dica rápida do dia 4 sobre engajamento nas redes sociais.",
    "Dica rápida do dia 5 sobre produtos digitais."
]

def gerar_todo_conteudo():
    """Gera vídeos e ebooks semanal + diários"""
    print("Gerando vídeos...")
    gerar_conteudo_semanal(texto_longo, textos_curtos)
    
    print("Gerando ebooks...")
    gerar_ebook_semanal(texto_longo, textos_curtos)
    
    print("Conteúdo gerado e salvo em 'output/' para aprovação humana.")

def aprovar_e_agendar_postagens():
    """Mostra postagens para aprovação e permite aprovar manualmente"""
    postagens = mostrar_postagens_para_aprovacao()
    if postagens:
        # Exemplo: aprovar todas as postagens (pode ser manual no futuro)
        for post in postagens:
            aprovar_postagem(post)
    return postagens

def registrar_vendas_exemplo():
    """Simula registro de vendas para marketing"""
    registrar_venda(100.0, "Venda de Ebook Instagram")
    registrar_venda(50.0, "Venda de Produto Afiliado TikTok")
    
    # Aprovar manualmente marketing
    aprovar_marketing(0)
    aprovar_marketing(1)

def gerar_relatorios_completos():
    """Gera relatórios em todos os períodos"""
    periodos = ["diario", "semanal", "mensal", "trimestral", "semestral", "anual"]
    for periodo in periodos:
        gerar_relatorio(periodo)

if __name__ == "__main__":
    # Passo 1: gerar vídeos e ebooks
    gerar_todo_conteudo()
    
    # Passo 2: mostrar e aprovar postagens
    aprovar_e_agendar_postagens()
    
    # Passo 3: registrar vendas e aprovar marketing
    registrar_vendas_exemplo()
    
    # Passo 4: gerar relatórios completos
    gerar_relatorios_completos()
    
    print("Fluxo completo executado! Todo o conteúdo está pronto para publicação e análise.")
