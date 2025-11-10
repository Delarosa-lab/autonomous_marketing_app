
import random

# Lista de produtos de exemplo (em produção, pode buscar de Hotmart, Amazon, Eduzz)
produtos = [
    {"nome": "Curso de Marketing Digital", "link": "https://www.hotmart.com"},
    {"nome": "Ebook de Produtividade", "link": "https://www.amazon.com"},
    {"nome": "Ferramenta de Edição de Vídeo", "link": "https://www.eduzz.com"},
]

def buscar_produto_vencedor():
    """
    Seleciona aleatoriamente um produto vencedor da lista.
    Em produção, aqui pode usar IA gratuita ou APIs para buscar produtos em alta.
    """
    produto = random.choice(produtos)
    return produto

def gerar_roteiro_produto(produto):
    """
    Gera um roteiro simples baseado no produto selecionado.
    Pode ser usado para vídeo longo, curtos ou ebook.
    """
    roteiro = f"""
    Hoje vamos apresentar: {produto['nome']}
    
    Descubra como ele pode transformar sua vida e aumentar seus resultados.
    
    Para mais informações ou adquirir, acesse: {produto['link']}
    
    Este conteúdo é totalmente gratuito e criado automaticamente para você.
    """
    return roteiro

if __name__ == "__main__":
    p = buscar_produto_vencedor()
    roteiro = gerar_roteiro_produto(p)
    print("Produto vencedor:", p["nome"])
    print("Roteiro gerado:\n", roteiro)
