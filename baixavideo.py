#IMPORTS NECESSARIOS
from pytube import YouTube
import pyautogui
from os import path
#PEGANDO O PATH
main = path.join(path.expanduser("~"))

while(True):
    url = pyautogui.prompt("Cole a url aqui:")
    video = YouTube(url)
    stream = video.streams.get_highest_resolution() #BAIXANDO O VIDEO NA MELHOR RESOLUÇAO POSSIVEL

    stream.download(output_path=main+'\\Videos') #SALVANDO NA PASTA VIDEOS DO WINDOWS
    pyautogui.alert("Video baixado!")
