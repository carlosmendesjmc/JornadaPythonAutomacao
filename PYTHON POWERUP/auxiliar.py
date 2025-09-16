import pyautogui
import time


# Aguarda um tempo pra mover o mouse ate a posição que deseja captar 
time.sleep(10)

#capta a posição do mouse e imprime no terminal
print(pyautogui.position())