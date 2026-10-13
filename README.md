# Python - YouTube Music Downloader

A small personal project made with Python to download audio from YouTube videos and playlists and convert it to MP3 using FFmpeg.

This project was created for educational purposes, as a way to practice Python and learn how to use external libraries.

## Features

- Download audio from a single video.
- Download playlists.
- Convert audio to MP3 with a quality setting of 192 kbps.
- Automatically save playlist audio files in folders named after the playlist.
- Continue processing a playlist when an error occurs with one of its items.

## Technologies Used

- **Python** — the main programming language.
- **yt-dlp** — for extracting and downloading audio.
- **FFmpeg** — for converting audio files to MP3.

## Requirements

Before running the program, you need to install:

- Python 3.10 or later.
- The `yt-dlp` library.
- FFmpeg, with audio conversion support.

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/guilhermy-de-oliveira/python-youtube-music-downloader.git
cd REPOSITORY_FOLDER
```

Replace `REPOSITORY_URL` and `REPOSITORY_FOLDER` with your repository URL and folder name.

**2. Install the Python dependency**

```bash
python -m pip install -U "yt-dlp[default]"
```

**3. Install FFmpeg**

Download FFmpeg from the official website:

https://ffmpeg.org/

Configure the executable so the program can find it. By default, this project expects to find `ffmpeg.exe` at `./bin/ffmpeg.exe`, relative to the directory from which the program is run.

## How to Use

Run the program:

```bash
python main.py
```

In the main menu, choose one of the following options:

- `1` — download audio from a single video.
- `2` — download audio from a playlist.

Then, enter the corresponding URL.

The audio files will be saved in the program's working directory. For playlists, a folder named after the playlist will be created.

## Notes

- The program was developed and tested on Windows 11.
- FFmpeg must be installed and available at the path configured in the code.
- This is a simple project and errors may occur depending on the URL, content availability, or changes to YouTube and the tools used.
- This repository does not include the FFmpeg executable or the downloaded audio files.

## Responsible Use

This project is intended for educational and personal use. Only use it with content you are authorized to download, and respect copyright laws and the platform's terms of service.

## Project Goal

This project is part of my programming learning journey. It was created to practice Python, working with external libraries, basic error handling, and audio processing.

Suggestions and contributions are very welcome.

Thank you for reading!
