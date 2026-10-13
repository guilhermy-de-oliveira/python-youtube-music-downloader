# DEPENDENCIES:
# Microsoft C++ Build Tools (MSVC v14x,  Windows 10/11 SDK)
# pip install -U "yt-dlp[default]"
# Download ffmpeg from https://www.ffmpeg.org/
# For ffmpeg, install the compiled build and copy the bin folder to this directory.

# Library to download videos from YouTube
from yt_dlp import YoutubeDL

# Function to download a playlist
def download_playlist(url_playlist):
    # YoutubeDL parameters
    ydl_opts = {
        # Audio quality format
        'format': 'bestaudio/best',
        # Extracts and converts to MP3 using FFmpeg
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            # Audio quality in kbps
            'preferredquality': '192',
        }],
        # Saves inside a folder named after the playlist
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
        # Ignore errors on specific videos so the whole playlist doesn't stop
        'ignoreerrors': True,
        # Location of ffmpeg
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

# Function to download a song
def download_music(url_video):
    # Settings to download audio only and convert to MP3
    ydl_opts = {
        # Audio quality format
        'format': 'bestaudio/best',
        # Extracts and converts to MP3 using FFmpeg
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            # Audio quality in kbps
            'preferredquality': '192',
        }],
        # Saves in the executable's folder with the video's title
        'outtmpl': '%(title)s.%(ext)s',
        # Location of ffmpeg
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

# Execution
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
