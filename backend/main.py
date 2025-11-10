
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
    
