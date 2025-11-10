
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Autonomous Marketing App")

# Permitir comunicação com frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Aplicativo de Marketing Autônomo iniciado!"}

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Pastas de conteúdo
VIDEO_FOLDER = "../output/videos"
EBOOK_FOLDER = "../output/ebooks"
# Listar vídeos para aprovação
@app.get("/api/videos")
def listar_videos():
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]
    return JSONResponse(content=videos)

# Listar ebooks para aprovação
@app.get("/api/ebooks")
def listar_ebooks():
    ebooks = [f for f in os.listdir(EBOOK_FOLDER) if f.endswith(".pdf")]
    return JSONResponse(content=ebooks)

# Aprovar um vídeo (simples exemplo)
@app.post("/api/videos/aprovar/{nome_video}")
def aprovar_video(nome_video: str):
    # Aqui apenas retorna sucesso (pode ser expandido para registrar aprovação)
    return {"message": f"Vídeo {nome_video} aprovado com sucesso"}

# Aprovar um ebook
@app.post("/api/ebooks/aprovar/{nome_ebook}")
def aprovar_ebook(nome_ebook: str):
    return {"message": f"Ebook {nome_ebook} aprovado com sucesso"}
    
from marketing_agent import marketing_aprovado, aprovar_marketing, gerar_relatorio

# Listar vendas pendentes para marketing
@app.get("/api/marketing/vendas")
def listar_vendas():
    return marketing_aprovado

# Aprovar investimento de marketing
@app.post("/api/marketing/aprovar/{indice}")
def aprovar_investimento(indice: int):
    if 0 <= indice < len(marketing_aprovado):
        aprovar_marketing(indice)
        return {"message": f"Investimento {indice} aprovado"}
    return {"error": "Índice inválido"}

# Gerar relatório
@app.get("/api/marketing/relatorio/{periodo}")
def relatorio_marketing(periodo: str):
    gerar_relatorio(periodo)
    return {"message": f"Relatório {periodo} gerado"}
from datetime import datetime, timedelta

# Estrutura de postagens agendadas
postagens_agendadas = []

# Listar postagens pendentes de aprovação
@app.get("/api/postagens")
def listar_postagens():
    # Lê vídeos e ebooks do output
    videos = [f for f in os.listdir("../output/videos") if f.endswith(".mp4")]
    ebooks = [f for f in os.listdir("../output/ebooks") if f.endswith(".pdf")]
    postagens = []

    redes = ["Instagram", "TikTok", "Kwai"]
    horarios = ["09:00", "12:00", "15:00", "18:00", "21:00"]

    for rede in redes:
        for i, video in enumerate(videos):
            postagens.append({
                "tipo": "vídeo",
                "arquivo": video,
                "rede_social": rede,
                "horario_sugerido": horarios[i % len(horarios)],
                "aprovado": False
            })
        for i, ebook in enumerate(ebooks):
            postagens.append({
                "tipo": "ebook",
                "arquivo": ebook,
                "rede_social": rede,
                "horario_sugerido": horarios[i % len(horarios)],
                "aprovado": False
            })
    return postagens

# Aprovar e agendar postagem
@app.post("/api/postagens/aprovar/{indice}")
def aprovar_postagem(indice: int):
    postagens = listar_postagens()
    if 0 <= indice < len(postagens):
        post = postagens[indice]
        post["aprovado"] = True
        # Define horário de publicação exato (futuro: integração real com API)
        post["data_agendada"] = datetime.now().strftime("%Y-%m-%d") + " " + post["horario_sugerido"]
        postagens_agendadas.append(post)
        return {"message": f"Postagem aprovada e agendada: {post}"}
    return {"error": "Índice inválido"}

# Listar postagens agendadas
@app.get("/api/postagens/agendadas")
def listar_agendadas():
    return postagens_agendadas
