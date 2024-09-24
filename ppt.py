'''
Jogo do pedra-papel-tesoura
2024.08.13
Sophia Bueno Cunha
'''

#--> Bibliotecas

#importa um valor inteiro aleatorio
from random import randint
#importa funçoes de modules
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
#tempo:
from time import sleep

#--> Constantes,Variaveis e Listas:

msgsInicio = ['Seja Bem Vindo ao', 'Jogo do PEDRA-PAPEL-TESOURA', 'Desenvolvido por Sophia Bueno Cunha', 'BOA SORTE! :3'] # Define uma lista de mensagens de boas-vindas que serão exibidas ao iniciar o jogo.
msgs = []
playAgain = '' # Inicializa uma variável para armazenar a escolha do usuário sobre jogar novamente. Está vazia no início.
playerScore = 0
computerScore = 0

#--> Funções 
def startPPT(): #função para iniciar o jogo
  while(True): # Inicia um loop que continuará enquanto a condição for verdadeira.
    clrScreen() # Limpa a tela do terminal.
    displayHeader(msgsInicio) # Exibe o cabeçalho com as mensagens de boas-vindas.
    playPPT()
    #função para começar o jogo
    playAgain = getUserOption ('Deseja jogar novamente [s/n]') # Solicita ao usuário se ele deseja jogar novamente e armazena a resposta em 'playAgain'.
    while not validateUserOption (playAgain, ['s', 'n', 'S', 'N']):   # Valida a resposta do usuário, garantindo que ela esteja entre as opções aceitáveis.
      playAgain = getUserOption('Deseja jogar novamente [s/n]')  # Se a resposta não for válida, solicita novamente a resposta.
    if playAgain.lower() != 's': # Verifica se a resposta do usuário não é 's' (ou 'S' ou 'y'/'Y' em qualquer caso).
      break  # Se a resposta for diferente de 's', o loop será interrompido e o jogo terminará.

def displayMenu(): #Define e exibe o menu de opções (Pedra, Papel, Tesoura) para o usuário.
  msgs = ['Escolha: ', 
    '[0] -> Pedra',
    '[1] -> Papel',
    '[2] -> Tesoura'] ##Uma lista é criada com as opções que o jogador pode escolher: Pedra, Papel ou Tesoura.
  displayLine() #Exibe uma linha de separação antes e depois das opções, melhorando a interface visual.
  for msg in msgs: #Para cada mensagem em 'msgs', a função 'displayMsg' é chamada para exibir a mensagem no terminal:
    displayMsg(msg)
  displayLine()


def displayScore(typeScore, playerScore, computerScore): #Exibe a pontuação atual ou final do jogo. typeScore define o tipo de placar (parcial ou final).
  msgs = [] #Cria uma lista de mensagens a serem exibidas. O primeiro item é typeScore (que pode ser "PLACAR" ou "PLACAR FINAL"), e o segundo é a string formatada mostrando as pontuações do jogador e do computador:
  msgs.append(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs) #Exibe as mensagens formatadas, provavelmente com algum tipo de estilização específica.
  
def determineWinner(playerChoice, computerChoice): #Avalia o resultado da rodada. Converte as escolhas do jogador e do computador em str representando Pedra, Papel, ou Tesoura:

  play = ''
  result = ''
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr = choices[int(computerChoice)]
  if playerChoice == computerChoice:
    #Determina o vencedor da rodada com base nas regras do jogo. Se as escolhas forem iguais, é empate; caso contrário, verifica qual escolha vence a outra:
    result = 'Empate!' #Se as escolhas forem iguais, a rodada é um empate.

  elif(playerChoice =='0' and computerChoice =='2') or (playerChoice =='1' and computerChoice =='0') or (playerChoice =='2' and computerChoice=='1'):
    play = f"{playerChoiceStr} vence {computerChoiceStr}"
    result = 'Você Ganhou!' #Condições de Vitória: Verifica todas as combinações em que o jogador vence. Se a escolha do jogador vence a do computador, play é definido para descrever essa vitória, e result é definido como "Você Ganhou!".
  else:
    play = f'{computerChoiceStr} vence {playerChoiceStr}'
    result = 'Você Perdeu!' #Se nenhuma das condições de vitória for atendida, significa que o jogador perdeu, e result é definido como "Você Perdeu!"
    
# Armazena as jogadas e o resultado em uma lista e exibe o resultado. Retorna o resultado da rodada (Vitória, Derrota, ou Empate):
  msgs = ['Jogada do Player: ' + playerChoiceStr, 
         'Jogada do PC: ' + computerChoiceStr,
         play, result]
  displayHeaderT(msgs)
  return result #A função retorna o resultado da rodada, indicando se o jogador ganhou, perdeu ou empatou.
  

def playPPT():#Inicializa a pontuação para uma nova partida
  playerScore = 0
  computerScore = 0
  #Enquanto nenhum dos jogadores atingir 2 pontos, continua a partida. Solicita a escolha do jogador e gera a escolha do computador:
  while playerScore < 2 and computerScore < 2: #Continua executando rodadas enquanto nem o jogador nem o computador tenham alcançado 2 pontos.
    displayMenu() #Chama displayMenu para mostrar as opções de Pedra, Papel e Tesoura ao jogador.
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0', '1', '2']): #O jogador faz uma escolha (0, 1 ou 2), e a entrada é validada até garantir que seja válida.
      
#Usando randint, o computador faz uma escolha aleatória entre 0, 1 e 2:
      displayMenu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
    result = determineWinner(playerChoice, computerChoice) #Chama determineWinner para decidir quem venceu a rodada.
    
    #Incrementa a pontuação do jogador ou do computador com base no resultado da rodada:
    if 'Ganhou' in result:
      playerScore += 1 #Se o jogador ganhou a rodada, sua pontuação é incrementada.
    elif 'Perdeu' in result:
      computerScore += 1 #Se o jogador perdeu a rodada, a pontuação do PC é incrementada.
    if playerScore < 2 and computerScore < 2: #Se nenhum dos jogadores atingiu 2 pontos, exibe o placar atual e pausa brevemente antes da próxima rodada:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
    # Exibe o placar final. Se o jogador vencer, exibe uma mensagem de vitória; caso contrário, exibe uma mensagem de derrota:
  displayScore ('PLACAR FINAL', playerScore, computerScore) #CEsta função é chamada para exibir o placar final do jogo.
  if playerScore > computerScore: #Aqui, o código verifica se a pontuação do jogador (playerScore) é maior que a do computador (computerScore).
    displayHeader(['Parabéns!! <3','VOCÊ VENCEU!']) #Se o jogador venceu, esta função é chamada para exibir uma mensagem de vitória na tela.
  else:
    displayHeader(['AFF','VOCÊ PERDEU!']) #Se a condição playerScore > computerScore for falsa (ou seja, o jogador não ganhou), o bloco else é executado, então neste caso, uma mensagem de derrota é exibida.

#--> Main