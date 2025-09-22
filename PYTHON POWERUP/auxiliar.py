import pyautogui
import time


# Aguarda um tempo pra mover o mouse ate a posição que deseja captar 
time.sleep(10)

#Clicando 7x na na barra de scroll
##pyautogui.click(x=1908, y=999, clicks=7)


# Aguarda um tempo pra mover o mouse ate a posição que deseja captar 
## time.sleep(10)

#capta a posição do mouse e imprime no terminal
print(pyautogui.position())