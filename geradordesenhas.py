import random
import pyautogui

caracteres_maiusc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caracteres_minusc = 'abcdefghijklmnopqrstuvwxyz'
caracteres_numespec = '0123456789!@#$%*'
lenght = 12

pyautogui.alert("Sua senha é: "+"".join(random.sample(caracteres_maiusc +
                                                      caracteres_minusc +
                                                      caracteres_numespec,
                                                      lenght)))
