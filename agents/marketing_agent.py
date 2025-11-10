import os
from datetime import datetime

# Pasta para armazenar relatórios
REPORTS_FOLDER = "reports"
os.makedirs(REPORTS_FOLDER, exist_ok=True)

# Exemplo de registro de monetização
monetizacao_total = 0.0
marketing_aprovado = []

def registrar_venda(valor, origem):
    """
    Registra uma venda e calcula 20% para marketing.
    """
    global monetizacao_total
    monetizacao_total += valor
    valor_marketing = valor * 0.2
    registro = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "origem": origem,
        "valor_venda": valor,
        "valor_marketing": valor_marketing,
        "aprovado": False
    }
    marketing_aprovado.append(registro)
    print(f"Venda registrada: {valor} de {origem}, {valor_marketing} destinado a marketing (aguardando aprovação)")

def aprovar_marketing(indice):
    """
    Aprova manualmente um investimento de marketing
    """
    if 0 <= indice < len(marketing_aprovado):
        marketing_aprovado[indice]["aprovado"] = True
        print(f"Investimento de marketing aprovado: {marketing_aprovado[indice]}")
    else:
        print("Índice inválido")

def gerar_relatorio(periodo="diario"):
    """
    Gera relatório resumido de vendas e marketing.
    Periodo pode ser: diario, semanal, mensal, trimestral, semestral, anual
    """
    relatorio_path = os.path.join(REPORTS_FOLDER, f"relatorio_{periodo}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(relatorio_path, "w", encoding="utf-8") as f:
        f.write(f"Relatório {periodo}\n")
        f.write("="*40 + "\n")
        total_vendas = 0
        total_marketing = 0
        for registro in marketing_aprovado:
            f.write(f"Data: {registro['data']}, Origem: {registro['origem']}, Valor venda: {registro['valor_venda']}, Valor marketing: {registro['valor_marketing']}, Aprovado: {registro['aprovado']}\n")
            total_vendas += registro['valor_venda']
            if registro['aprovado']:
                total_marketing += registro['valor_marketing']
        f.write("="*40 + "\n")
        f.write(f"Total vendas: {total_vendas}\n")
        f.write(f"Total marketing aprovado: {total_marketing}\n")
    print(f"Relatório gerado: {relatorio_path}")

if __name__ == "__main__":
    # Exemplo de uso
    registrar_venda(100.0, "Venda de Ebook Instagram")
    registrar_venda(50.0, "Venda de Produto Afiliado TikTok")
    
    # Aprovar manualmente a primeira venda para marketing
    aprovar_marketing(0)
    
    # Gerar relatório diário
    gerar_relatorio("diario")
