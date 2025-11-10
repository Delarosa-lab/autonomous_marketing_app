from product_agent import buscar_produto_vencedor, gerar_roteiro_produto
from video_agent import gerar_conteudo_semanal
from ebook_agent import gerar_ebook_semanal
from social_agent import mostrar_postagens_para_aprovacao, aprovar_postagem
from marketing_agent import registrar_venda, aprovar_marketing, gerar_relatorio
import random

def fluxo_completo():
    print("=== INÍCIO DO FLUXO SEMANAL/DIA ===")

    # 1. Seleciona produto vencedor
    produto_semanal = buscar_produto_vencedor()
    print("Produto vencedor da semana:", produto_semanal["nome"])

    # 2. Gera roteiros
    texto_longo = gerar_roteiro_produto(produto_semanal)
    textos_curtos = [f"{produto_semanal['nome']} - dica rápida {i+1}" for i in range(5)]

    # 3. Gera vídeos
    print("Gerando vídeos...")
    gerar_conteudo_semanal(texto_longo, textos_curtos)

    # 4. Gera ebooks
    print("Gerando ebooks...")
    gerar_ebook_semanal(texto_longo, textos_curtos)

    # 5. Mostra postagens pendentes para aprovação humana
    print("Postagens pendentes para aprovação:")
    postagens = mostrar_postagens_para_aprovacao()
    # Aqui o humano aprovará no painel React, ou pode-se aprovar manualmente:
    for post in postagens:
        aprovar_postagem(post)

    # 6. Registrar vendas simuladas e calcular marketing
    print("Registrando vendas e marketing...")
    for i, texto in enumerate([texto_longo]+textos_curtos):
        valor_venda = random.randint(20, 100)
        origem = f"Venda {i+1} - {produto_semanal['nome']}"
        registrar_venda(valor_venda, origem)

    # Aprovar marketing manualmente (exemplo)
    for idx in range(len([texto_longo]+textos_curtos)):
        aprovar_marketing(idx)

    # 7. Gerar relatórios completos
    print("Gerando relatórios...")
    periodos = ["diario", "semanal", "mensal", "trimestral", "semestral", "anual"]
    for periodo in periodos:
        gerar_relatorio(periodo)

    print("=== FLUXO COMPLETO EXECUTADO COM SUCESSO ===")

if __name__ == "__main__":
    fluxo_completo()
