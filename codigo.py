# Passo 1: Abrir o sistema da Empresa
#    Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados dos produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4

# Bibliotecas
# pyautogui - Automatizar o teclado e o mouse -> pip install pyautogui
# pandas - Trabalhar com arquivos de dados
# time - Controlar o tempo do programa


import pyautogui
import time
import pandas 


# Passo 1: Abrir o sistema da Empresa
pyautogui.PAUSE = 0.5   

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1) # esperar 1 segundo

# Passo 2: Fazer login
pyautogui.click(x=-1244, y=415)
pyautogui.write('suiane.henrichs@yahoo.com.br')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('enter')

# Passo 3: Importar a base de dados dos produtos
pandas.read_csv('produtos.csv')
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 produto

for linha in tabela.index: # Para cada linha da tabela, execute o código abaixo
    pyautogui.click(x=-1250, y=302) # Clicar no primeiro campo

    # codigo do produto
    codigo = tabela.loc[linha, 'codigo'] 
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # Marca do produto
    marca = tabela.loc[linha, 'marca'] 
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # Tipo do produto
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # Categoria do produto
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço Unitário do Produto
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # Custo do Produto
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # Observações
    obs = str(tabela.loc[linha, 'obs']) 
    if obs != "nan": # Se a observação não for vazia
        pyautogui.write(obs) # Escreva a observação
    pyautogui.press('tab')

    # Salvar
    pyautogui.press('enter')

    pyautogui.scroll(1000) # Rolar a tela para baixo


