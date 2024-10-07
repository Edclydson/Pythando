# IMPORTS NECESSARIOS
from pytubefix import YouTube
from pytubefix.cli import on_progress
import pyautogui
from os import path
# PEGANDO O PATH
main = path.join(path.expanduser("~"))

while True:
    url = pyautogui.prompt("Cole a url aqui:")
    video = YouTube(url, on_progress_callback=on_progress)
    # BAIXANDO O VIDEO NA MELHOR RESOLUÇAO POSSIVEL
    stream = video.streams.get_highest_resolution()

    # SALVANDO NA PASTA VIDEOS DO WINDOWS
    stream.download(output_path=main+'\\Videos')
    pyautogui.alert("Video baixado!")
