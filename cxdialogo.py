import pyautogui
var = pyautogui.prompt("Digite seu nome!")  # recebe o que usuario digita
pyautogui.alert("Olá,"+var+"!")  # alert exibe ola nome do usuario
