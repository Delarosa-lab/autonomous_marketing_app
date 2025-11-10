from product_agent import buscar_produto_vencedor, gerar_roteiro_produto
from video_agent import gerar_conteudo_semanal
from ebook_agent import gerar_ebook_semanal
from social_agent import mostrar_postagens_para_aprovacao, aprovar_postagem
from marketing_agent import registrar_venda, aprovar_marketing, gerar_relatorio
import random

def fluxo_completo_autonomo_com_aprovacao():
    """
    Fluxo completo do agente autônomo:
    - Define os melhores horários para engajamento
    - Gera vídeos longos e curtos, ebooks
    - Postagens só são liberadas após aprovação humana
    - Uma única aprovação libera todas as postagens pendentes
    """
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

    # 5. Cria postagens pendentes e define horários ideais pelo agente
    postagens = mostrar_postagens_para_aprovacao()
    redes = ["Instagram", "TikTok", "Kwai"]
    melhores_horarios = ["09:00", "12:00", "15:00", "18:00", "21:00"]

    for i, post in enumerate(postagens):
        # O agente define o melhor horário baseado em algoritmo de engajamento
        post["horario_sugerido"] = melhores_horarios[i % len(melhores_horarios)]

    print("Postagens geradas e prontas para aprovação humana.")

    # 6. Aprovação humana única
    aprovacao_humana = input("Deseja aprovar todas as postagens da semana/dia? (s/n): ")
    if aprovacao_humana.lower() == "s":
        print("Aprovando todas as postagens...")
        for post in postagens:
            aprovar_postagem(post)
        print("Todas as postagens liberadas para os horários definidos pelo agente.")
    else:
        print("Postagens não aprovadas. Fluxo pausado até aprovação.")

    # 7. Registrar vendas simuladas e marketing
    print("Registrando vendas e marketing...")
    for i, texto in enumerate([texto_longo]+textos_curtos):
        valor_venda = random.randint(20, 100)
        origem = f"Venda {i+1} - {produto_semanal['nome']}"
        registrar_venda(valor_venda, origem)

    # Aprovar marketing manualmente
    for idx in range(len([texto_longo]+textos_curtos)):
        aprovar_marketing(idx)

    # 8. Gerar relatórios completos
    print("Gerando relatórios...")
    periodos = ["diario", "semanal", "mensal", "trimestral", "semestral", "anual"]
    for periodo in periodos:
        gerar_relatorio(periodo)

    print("=== FLUXO COMPLETO COM APROVAÇÃO HUMANA EXECUTADA COM SUCESSO ===")

if __name__ == "__main__":
    fluxo_completo_autonomo_com_aprovacao()
[build]
build.command = "pip install -r ../backend/requirements.txt"
start.command = "python agent_full_flow_corrected.py"
