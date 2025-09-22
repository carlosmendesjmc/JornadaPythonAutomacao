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
time.sleep(2)

# Passo 2: Fazer login

# Fazer Login no site da empresa com as credencias e colocar senha
# Clica na posiçao onde esta o campo que sera digitado o email
pyautogui.click(x=538, y=565) 


# Digita o email para logar

pyautogui.write("carlosmendesjmc@gmail.com")

# Espere 3 Segundos
time.sleep(2)

# Clica na posiçao onde esta o campo que sera digitado a senha
pyautogui.click(x=539, y=705)

# Digita a senha para logar
pyautogui.write("12345")

#pressionar enter para logar
pyautogui.press("enter")

# Espere 3 Segundos
time.sleep(2)

# Passo 3: Importar a base de dados que sera cadastrado no sistema da empresa

# Importar a base de dados que vamos cadastrar
# Criamos esta variavel tabela pra receber os dados que vamos ler

tabela = pandas.read_csv("C:\\Temp\\JornadaPythonAutomacao\\produtos.csv")

print(tabela)


# Posso usar, pyautogui.scroll(100) -100  pracima ou pra baixo
# Passo 4: Cadastrar produto 1 no sistema

for linha in tabela.index:  # Para cada linha da minha tabela ele vai percorrer e exucutar a mesma ação

    # Código do Produto
    pyautogui.click(x=615, y=390)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)


    # Marca do Produto
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    # Tipo do Produto
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    # Categoria do Produto
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    # Preço Unitário do Produto
    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))

    #Clicando 7x na na barra de scroll
    pyautogui.click(x=1908, y=999, clicks=7)  # clicks=7 

    # Custo do Produto
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    # OBS
    pyautogui.press("tab")
    obs = (tabela.loc[linha, "obs"])
    #if pandas.notna(obs):
    #if obs != "nan":
    
    if pandas.isna(obs) or str(str).lower() == "nan":
        pyautogui.write("obs")
    else:
        pyautogui.write(str(obs))
        
    pyautogui.press("tab")

    # Clicando no botão de enviar/cadastrar
    pyautogui.press("enter")
    
    pyautogui.sleep(1)
    
    pyautogui.scroll(1000)


# passo 5: repetir o mesmo passo para cadastrar todos produtos no sistema da empresa

# Para pausar a automação coloque o mouse no canto esquerdo da tela e aguarde é como fazer um FAILSAFE





