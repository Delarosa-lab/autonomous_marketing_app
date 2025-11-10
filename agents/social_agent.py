import os
from datetime import datetime, timedelta

# Pasta onde estão os conteúdos para aprovação
VIDEO_FOLDER = "output/videos"
EBOOK_FOLDER = "output/ebooks"

# Lista de redes sociais suportadas
REDES_SOCIAIS = ["Instagram", "TikTok", "Kwai"]

# Horários sugeridos para postagens (exemplo, pode ser ajustado)
HORARIOS_DE_ENGAJAMENTO = ["09:00", "12:00", "15:00", "18:00", "21:00"]

def listar_conteudos():
    """Lista todos os vídeos e ebooks disponíveis para aprovação"""
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]
    ebooks = [f for f in os.listdir(EBOOK_FOLDER) if f.endswith(".pdf")]
    return videos, ebooks

def preparar_postagens():
    """
    Prepara a lista de postagens para cada rede social,
    mas não posta nada sem aprovação humana.
    """
    videos, ebooks = listar_conteudos()
    postagens = []

    for rede in REDES_SOCIAIS:
        for i, video in enumerate(videos):
            postagem = {
                "rede_social": rede,
                "tipo": "vídeo",
                "arquivo": os.path.join(VIDEO_FOLDER, video),
                "aprovado": False,  # só posta após aprovação
                "horario_sugerido": HORARIOS_DE_ENGAJAMENTO[i % len(HORARIOS_DE_ENGAJAMENTO)]
            }
            postagens.append(postagem)

        for ebook in ebooks:
            postagem = {
                "rede_social": rede,
                "tipo": "ebook",
                "arquivo": os.path.join(EBOOK_FOLDER, ebook),
                "aprovado": False,
                "horario_sugerido": HORARIOS_DE_ENGAJAMENTO[i % len(HORARIOS_DE_ENGAJAMENTO)]
            }
            postagens.append(postagem)

    return postagens

def aprovar_postagem(postagem):
    """
    Marca uma postagem como aprovada pelo humano
    """
    postagem["aprovado"] = True
    print(f"Postagem aprovada para {postagem['rede_social']}: {postagem['arquivo']}")

def mostrar_postagens_para_aprovacao():
    """Mostra todas as postagens para o humano aprovar"""
    postagens = preparar_postagens()
    print("Postagens pendentes de aprovação:")
    for i, post in enumerate(postagens, start=1):
        print(f"{i}. {post['tipo']} - {post['arquivo']} - Rede: {post['rede_social']} - Horário sugerido: {post['horario_sugerido']} - Aprovado: {post['aprovado']}")
    return postagens

if __name__ == "__main__":
    # Exemplo de uso
    postagens = mostrar_postagens_para_aprovacao()
    
    # Aprovar manualmente a primeira postagem como exemplo
    if postagens:
        aprovar_postagem(postagens[0])
