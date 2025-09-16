import pyautogui 
import time
import pandas



# Vamos instalar no terminal aqui mesmo no VSCode --> pip install pyautogui
# pyautogui -> fazer automação com python

# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar em algum lugar
# pyautogui.hotkey -> apertar uma combinação de teclas / ex pyaoutogui.hotkey("ctrl", "c")


# Configuração de Pause para ter um tempo em todas as fases da execução 
pyautogui.PAUSE = 1


# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o Windows, menu iniciar
pyautogui.press("win")

# Escrever o texto chrome
pyautogui.write("chrome")

# Pressionar a tecla enter para abrir o chroome
pyautogui.press("enter")


# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# Pressionar a tecla enter para abrir o site da empresa
pyautogui.press("enter")

# Espere 3 Segundos
time.sleep(3)

# Fazer Login no site da empresa com as credencias e colocar senha
# Clica na posiçao onde esta o campo que sera digitado o email
pyautogui.click(x=538, y=565) 


# Digita o email para logar

pyautogui.write("carlosmendesjmc@gmail.com")

# Espere 3 Segundos
time.sleep(3)

# Clica na posiçao onde esta o campo que sera digitado a senha 
pyautogui.click(x=539, y=705) 

# Digita a senha para logar
pyautogui.write("12345")

#pressionar enter para logar
pyautogui.press("enter")

# Espere 3 Segundos
time.sleep(3)

# Importar a base de dados que vamos cadastrar
# Criamos esta variavel tabela pra receber os dados que vamos ler

tabela = pandas.read_csv("C:\Temp\JornadaPythonAutomacao\produtos.csv")

print(tabela)











# Passo 2: Fazer login
# Passo 3: Importar a base de dados que sera cadastrado no sistema da empresa
# Passo 4: Cadastrar produto 1 no sistema
# passo 5: repetir o mesmo passo para cadastrar todos produtos no sistema da empresa





