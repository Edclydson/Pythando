from pytube import YouTube
import pyautogui
from os import path
main = path.join(path.expanduser("~"))
while(True):
    url = pyautogui.prompt("Cole a url aqui:")
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    stream.download(output_path=main+'\\Videos')
    pyautogui.alert("Video baixado!")
