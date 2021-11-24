import random
import pyautogui

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%*'
lenght = 12
passwrd = "".join(random.sample(caracteres, lenght))
pyautogui.alert("Sua senha é: "+passwrd)
