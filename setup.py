import sys
import os
import shutil
import subprocess
from pathlib import Path

# Checks if a filepath exists
# When imported from common, it was throwing vlc import error
def doesItExist(path: str) -> bool:
    try:
        open(path, 'rb').close()
        exists = True
    except FileNotFoundError:
        exists = False
    finally:
        return exists

def install(name: str) -> None:
    subprocess.call([sys.executable, '-m', 'pip', 'install', name])

def youtube_download(url: str) -> None:
    subprocess.call([sys.executable, '-m', 'youtube_dl', '--extract-audio', '--audio-format=mp3', url])

# Create Music folder
try:
    os.mkdir(str(Path(os.getcwd()) / "Music"))
except FileExistsError:
    pass

# Libraries
install("python-vlc")
install("easygui")
install("youtube-dl")

# Audio Files
audio = {
    "giorno.mp3": "https://www.youtube.com/watch?v=tLyRpGKWXRs",
    "minecraft.mp3": "https://www.youtube.com/watch?v=cjQQ9JYGgTM",
    "oof.mp3": "https://www.youtube.com/watch?v=HoBa2SyvtpE"
}

for name in audio:
    filepath = Path(os.getcwd()) / "Music" / name
    if not doesItExist(str(filepath)):
        print("Downloading", name)
        youtube_download(audio[name])
        filename = [f for f in os.listdir(os.getcwd()) if '.mp3' in f][0]
        shutil.move(str(Path(os.getcwd()) / filename), filepath)
