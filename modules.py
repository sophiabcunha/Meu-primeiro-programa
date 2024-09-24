'''
Arquivo de Modulos
2024.08.13
Sophia Bueno Cunha
'''

#--> Bibliotecas
from random import choice
from time import sleep
#--> Constantes,Variaveis e Listas
TAM = 40 # Tamanho da tela
CAR = choice(['=', '*', '/', '+']) #  caracere utilizado para desenhar na tela
MAR = 4 #Tamanho da margem

#--> Funções 
def clrScreen(): #Função para limpar a tela
  print('\n'*TAM) # mostra na tela \n == Linha * TAM 

def displayLine(): #função para mostrar uma linha de caracteres
  print(CAR*TAM) # Imprime 'TAM' quebras de linha para limpar a tela do terminal.

def displayMsg(msg): #mostra uma mensagem alinhada entre o CAR
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') # Exibe a mensagem alinhada à esquerda dentro da linha, com margem 'MAR'.
def displayHeaderT(msgs):
  displayLine()
  for item in msgs:
    displayMsgCenter(item)
    sleep(1)
  displayLine() 
  
def displayMsgCenter(msg): # Função para mostrar uma mensagem centralizada entre o CAR
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') # Exibe a mensagem centralizada dentro da linha, com margem 'MAR'.


def displayHeader(msgs): # Função para exibir um cabeçalho com várias mensagens
  displayLine()  # Exibe uma linha de caracteres no topo.
  for item in msgs: # Itera sobre cada item na lista de mensagens.
    displayMsgCenter(item) # Exibe cada mensagem centralizada.
  displayLine() # Exibe uma linha de caracteres na parte inferior.

def getUserOption(msg): # Função para obter a opção do usuário
  option = input(f'{CAR} {msg}: ').strip() # Solicita uma entrada do usuário e remove espaços extras ao redor.
  return option

def validateUserOption(option, listOption): # Função para validar a opção do usuário
  if option in listOption: # Verifica se a opção fornecida está na lista de opções válidas.
    return True  # Verifica se a opção fornecida está na lista de opções válidas.
  else:
    msgErro = ['opção invalida!', 'escolha novamente'] # Mensagens de erro para opções inválidas.
    displayHeader(msgErro) # Exibe as mensagens de erro.
    return False # Retorna False se a opção não for válida.

#--> Main