
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
