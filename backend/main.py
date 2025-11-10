from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from social_agent import postagens_agendadas, mostrar_postagens_para_aprovacao, aprovar_postagem
from marketing_agent import marketing_aprovado, aprovar_marketing, gerar_relatorio, registrar_venda

app = FastAPI()

# Permite que o frontend acesse o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pastas de conteúdo
VIDEO_FOLDER = "../output/videos"
EBOOK_FOLDER = "../output/ebooks"

# Rotas de vídeos
@app.get("/api/videos")
def listar_videos():
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]
    return JSONResponse(content=videos)

@app.post("/api/videos/aprovar/{nome_video}")
def aprovar_video(nome_video: str):
    return {"message": f"Vídeo {nome_video} aprovado com sucesso"}

# Rotas de ebooks
@app.get("/api/ebooks")
def listar_ebooks():
    ebooks = [f for f in os.listdir(EBOOK_FOLDER) if f.endswith(".pdf")]
    return JSONResponse(content=ebooks)

@app.post("/api/ebooks/aprovar/{nome_ebook}")
def aprovar_ebook(nome_ebook: str):
    return {"message": f"Ebook {nome_ebook} aprovado com sucesso"}

# Rotas de marketing
@app.get("/api/marketing/vendas")
def listar_vendas():
    return marketing_aprovado

@app.post("/api/marketing/aprovar/{indice}")
def aprovar_investimento(indice: int):
    if 0 <= indice < len(marketing_aprovado):
        aprovar_marketing(indice)
        return {"message": f"Investimento {indice} aprovado"}
    return {"error": "Índice inválido"}

@app.get("/api/marketing/relatorio/{periodo}")
def relatorio_marketing(periodo: str):
    gerar_relatorio(periodo)
    return {"message": f"Relatório {periodo} gerado"}

# Rotas de postagens
@app.get("/api/postagens")
def listar_postagens():
    return mostrar_postagens_para_aprovacao()

@app.post("/api/postagens/aprovar/{indice}")
def aprovar_postagem_backend(indice: int):
    postagens = mostrar_postagens_para_aprovacao()
    if 0 <= indice < len(postagens):
        aprovar_postagem(postagens[indice])
        return {"message": f"Postagem {postagens[indice]['arquivo']} aprovada e liberada!"}
    return {"error": "Índice inválido"}

@app.get("/api/postagens/agendadas")
def listar_agendadas():
    return postagens_agendadas
