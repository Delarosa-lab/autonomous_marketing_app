
import os
from gtts import gTTS
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, AudioFileClip

# Definir pastas de saída
VIDEO_OUTPUT = "output/videos"
AUDIO_OUTPUT = "output/audios"

os.makedirs(VIDEO_OUTPUT, exist_ok=True)
os.makedirs(AUDIO_OUTPUT, exist_ok=True)

def gerar_audio(texto, nome_arquivo):
    """Cria áudio da narração em mp3"""
    caminho_audio = os.path.join(AUDIO_OUTPUT, nome_arquivo)
    tts = gTTS(text=texto, lang="pt")
    tts.save(caminho_audio)
    return caminho_audio

def gerar_video(texto, nome_arquivo, duracao=10):
    """Cria vídeo simples com fundo branco, áudio e legenda"""
    # Criar áudio
    audio_path = gerar_audio(texto, nome_arquivo.replace(".mp4", ".mp3"))

    # Criar vídeo com fundo branco
    clip = ColorClip(size=(720, 480), color=(255, 255, 255), duration=duracao)

    # Legenda
    txt_clip = TextClip(txt=texto, fontsize=24, color='black', size=(700, None), method='caption')
    txt_clip = txt_clip.set_position('center').set_duration(duracao)

    # Adicionar áudio
    audio_clip = AudioFileClip(audio_path)
    video = CompositeVideoClip([clip, txt_clip]).set_audio(audio_clip)

    # Salvar vídeo
    caminho_video = os.path.join(VIDEO_OUTPUT, nome_arquivo)
    video.write_videofile(caminho_video, fps=24)
    print(f"Vídeo salvo: {caminho_video}")

def gerar_conteudo_semanal(texto_semanal, textos_diarios):
    """Gera 1 vídeo longo semanal e 5 curtos diários"""
    # Vídeo longo semanal
    gerar_video(texto_semanal, "video_longo_semanal.mp4", duracao=20)

    # 5 vídeos curtos diários
    for i, texto in enumerate(textos_diarios, start=1):
        gerar_video(texto, f"video_curto_dia_{i}.mp4", duracao=10)

if __name__ == "__main__":
    # Exemplo de uso
    texto_longo = "Este é o vídeo longo semanal. Aqui você pode colocar o conteúdo completo."
    textos_curtos = [
        "Vídeo curto dia 1",
        "Vídeo curto dia 2",
        "Vídeo curto dia 3",
        "Vídeo curto dia 4",
        "Vídeo curto dia 5",
    ]
    gerar_conteudo_semanal(texto_longo, textos_curtos)
