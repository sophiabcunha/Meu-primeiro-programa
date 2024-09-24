'''
Jogo do Par ou Ímpar
2024.08.20
Sophia Bueno Cunha
'''

#--> Bibliotecas

from random import randint #randint da biblioteca random para gerar números aleatórios.
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT #Funções personalizadas de um módulo chamado modules que ajudam a organizar e exibir informações na tela, além de capturar e validar as opções do usuário.
from time import sleep #sleep da biblioteca time, utilizada para pausar a execução do programa por um curto período de tempo.


#--> Constantes, Variáveis e Listas:

msgsInicio = ['Seja Bem Vindo ao', 'Jogo do PAR OU ÍMPAR', 'Desenvolvido por Sophia Bueno Cunha', 'BOA SORTE! :3'] #armazenar mensagens de boas-vindas a serem exibidas no início do jogo.
playAgain = ''  #controlar se o jogador deseja ou não jogar novamente.

#playerScore e computerScore: armazenar a pontuação do jogador e do computador, respectivamente:
playerScore = 0
computerScore = 0 


#--> Funções 
#Esta função é a entrada principal do jogo:

def startParImpar(): #Limpa a tela e exibe o cabeçalho com as mensagens de boas-vindas:
  #Chama a função playParImpar, que executa o jogo.
    while(True):
        clrScreen() 
        displayHeader(msgsInicio) 
        playParImpar()

        playAgain = getUserOption('Deseja jogar novamente [s/n]') 
        while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']):  
            playAgain = getUserOption('Deseja jogar novamente [s/n]')  #Pergunta ao jogador se ele deseja jogar novamente e, se não desejar, encerra o loop e, consequentemente, o jogo.
        if playAgain.lower() != 's': 
            break 

def displayMenu(): #Esta função exibe um menu simples com as opções "Par" e "Ímpar" para o jogador escolher. A função usa displayLine para desenhar uma linha antes e depois das mensagens e displayMsg para exibir cada mensagem.
    msgs = ['Escolha: ',
            '[0] -> Par',
            '[1] -> Ímpar']
    displayLine()
    for msg in msgs:
        displayMsg(msg)
    displayLine()

def displayScore(typeScore, playerScore, computerScore):#exibe o placar atual ou final. Recebe como parâmetros o tipo de placar (typeScore), a pontuação do jogador e a do computador. As mensagens são montadas e passadas para a função displayHeaderT, que provavelmente as exibe de forma centralizada e destacada.
    msgs = []
    msgs.append(typeScore)
    msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
    displayHeaderT(msgs)

def determineWinner(playerChoice, playerNumber, computerNumber):#Esta função determina o vencedor da rodada:

    play = ''
    result = ''
    choices = ['PAR', 'ÍMPAR']
    playerChoiceStr = choices[int(playerChoice)] #Converte a escolha do jogador (playerChoice) em "PAR" ou "ÍMPAR".

    soma = playerNumber + computerNumber
    resultado = "PAR" if soma % 2 == 0 else "ÍMPAR" ##Soma o número escolhido pelo jogador e pelo computador e determina se o resultado é par ou ímpar.

    if resultado.lower() == playerChoiceStr.lower(): #Compara o resultado com a escolha do jogador para decidir se ele ganhou ou perdeu.
        result = 'Você Ganhou!'
    else:
        result = 'Você Perdeu!'#Exibe uma mensagem detalhada com as escolhas, soma e resultado final, retornando o resultado ("Você Ganhou!" ou "Você Perdeu!") para quem chamou a função.

    msgs = [f'Você escolheu {playerChoiceStr} e o número {playerNumber}', 
            f'O PC escolheu o número {computerNumber}',
            f'Soma: {soma} -> {resultado}',
            result]
    displayHeaderT(msgs)
    return result 

def playParImpar(): #Esta função encapsula a lógica do jogo em si:

  #Inicializa as pontuações do jogador e do computador.
  #Continua jogando rodadas até que um dos dois atinja a pontuação de 2, chamando displayMenu para mostrar as opções e capturar a escolha do jogador.
  #Chama determineWinner para decidir quem ganhou a rodada e atualiza as pontuações.
  #Mostra o placar atual entre as rodadas e, ao final, exibe o placar final e uma mensagem apropriada:
    playerScore = 0
    computerScore = 0
    while playerScore < 2 and computerScore < 2:
        displayMenu()
        playerChoice = getUserOption('Sua escolha')
        while not validateUserOption(playerChoice, ['0', '1']):
            displayMenu()
            playerChoice = getUserOption('Sua escolha')

        playerNumber = int(getUserOption('Escolha um número (0-10): '))
        computerNumber = randint(0, 10)

        result = determineWinner(playerChoice, playerNumber, computerNumber)

        if 'Ganhou' in result:
            playerScore += 1
        elif 'Perdeu' in result:
            computerScore += 1

        if playerScore < 2 and computerScore < 2:
            displayScore('PLACAR', playerScore, computerScore)
        sleep(1)

    displayScore('PLACAR FINAL', playerScore, computerScore)

    if playerScore > computerScore:
        displayHeader(['Parabéns!! <3','VOCÊ VENCEU!'])
    else:
        displayHeader(['AFF','VOCÊ PERDEU!'])

#--> Main

