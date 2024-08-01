import pyautogui
from time import sleep      #pausa a execução por alguns segundos
from mouseinfo import mouseInfo  #escrever no terminal e depois mouseInfo(


# passos manuais para realizar o processo
#1. clicar e digitar meu usuario
pyautogui.click(673,384, duration=2)
pyautogui.write("louyse")

# 2. clicar e digitar minha senha
pyautogui.click(676,410, duration=2)
pyautogui.write('1234')

# 3. clicar em entrar
pyautogui.click(587,441, duration=2)

# 4. extrair cada produto
with open("produtos.txt","r") as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
    
#    4.1 clicar e digitar produto
pyautogui.click(392,371, duration=2)
pyautogui.write(produto)
# 	 4.2 clicar e digitar quantidade
pyautogui.click(397,398, duration=2)
pyautogui.write(quantidade)
# 	 4.3 clicar e digitar preço
pyautogui.click(403,424, duration=2)
pyautogui.write(preco)

# 	 4.4 clicar em registrar
pyautogui.click(316,582, duration=1)
sleep(1)

