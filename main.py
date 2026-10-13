# DEPENDENCIES:
# Microsoft C++ Build Tools (MSVC v14x,  Windows 10/11 SDK)
# pip install -U "yt-dlp[default]"
# Download ffmpeg in https://www.ffmpeg.org/
# For ffmpeg, install it compiled and copy & paste the bin folder to this directory.

# Biblioteca para baixar vídeos do Youtube
from yt_dlp import YoutubeDL

# Função para baixar uma playlist
def download_playlist(url_playlist):
    # Parametros do YoutubeDL
    ydl_opts = {
        # Formato de qualidade do áudio
        'format': 'bestaudio/best',
        # Extrai e converte para MP3 usando o FFmpeg
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            # Qualidade do áudio em kbps
            'preferredquality': '192',
        }],
        # Salva dentro de uma pasta com o nome da playlist
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
        # Ignora erros em vídeos específicos para não travar a playlist inteira
        'ignoreerrors': True,
        # Localização do ffmpeg
        'ffmpeg_location': './bin/ffmpeg.exe',
        'remote-components': 'ejs:github',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print('Analysing playlist and starting the downloads...')
            ydl.download([url_playlist])
            print('\nFinished!')
    except Exception as e:
        print(f'Error: {e}')

# Função de baixar uma música
def download_music(url_video):
    # Configurações para baixar apenas o áudio e converter para MP3
    ydl_opts = {
        # Formato de qualidade do áudio
        'format': 'bestaudio/best',
        # Extrai e converte para MP3 usando o FFmpeg
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            # Qualidade do áudio em kbps
            'preferredquality': '192',
        }],
        # Salva na pasta do executável com o nome do vídeo
        'outtmpl': '%(title)s.%(ext)s',
        # Localização do ffmpeg
        'ffmpeg_location': './bin/ffmpeg.exe',
        'remote-components': 'ejs:github',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print('Starting the download...')
            ydl.download([url_video])
            print('Download and conversion successfully completed!')
    except Exception as e:
        print(f'Error: {e}')

# Execução
if __name__ == '__main__':
    print("Python - Youtube Music Downloader:")
    print(
        "Want download a:\n" \
        "[1] Single Music\n" \
        "[2] Playlist\n"
    )
    option = input('> ')
    match option:
        # [1] Single Music
        case "1":
            print('\n Paste a Youtube Video URL:\n')
            url = input('> ')
            download_music(url)
        # [2] Playlist
        case "2":
            print('\n Paste a Youtube Playlist URL:\n')
            url = input('> ')
            download_playlist(url)
