from pytube import YouTube
import pyautogui
url = pyautogui.prompt("Cole a url aqui:")
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path='ADICIONA AQUI CAMINHO DA PASTA')
