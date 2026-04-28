# Regras:

# O jogo será jogado em um tabuleiro 3x3.
# Dois jogadores, X e O, escolhem uma marcação cada um.
# Os jogadores alternam suas jogadas, colocando sua marcação em uma célula vazia.
# O jogo termina quando um jogador consegue uma linha, coluna ou diagonal completa com sua marcação ou se todas as células estiverem preenchidas sem um vencedor.

# Estrutura do Programa:

# Crie uma função para exibir o tabuleiro.
# Crie uma função para verificar se houve um vencedor.
# Crie uma função para verificar se houve um empate.
# Crie uma função para verificar se uma jogada é válida.
# Implemente o loop principal do jogo, onde os jogadores alternam suas jogadas até que haja um vencedor ou um empate.


#Criar tabuleiro
def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

#criação de uma matriz 3x3
#cria uma linha do tabuleiro: repete 3 vezes a ação de criar um espaço vazio, ou seja, resulta em uma linha de 3 posições vazias [" "," "," "]
#repete a criação da linha com 3 espaços vazios 3 vezes, ou seja, cria 3 linhas com 3 colunas vazias e as junta dentro de uma lista mestra


#Exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("\n") #separa as mensagens anteriores da exibição do tabuleiro
    for i in range(3):
        #acessa cada coluna (0, 1 e 2) da linha atual (i) manualmente, de acordo com a volta em que o loop está
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ") #os segundos colchetes, [0],[1] e [2] referem-se as colunas
        if i < 2:
            print("---+---+---") #linha divisória
    print("\n")


#Crie uma função para verificar se houve um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # CONFERE SE TEM VENCEDOR PELAS LINHAS
    for i in range(3):
        #se todos os elementos da linha 'i' forem iguais ao jogador, tem 3 X ou 3 O na mesma linha, ou seja, jogador venceu
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True #indica que tem vencedor

    # CONFERE SE TEM VENCEDOR PELAS COLUNAS
    for i in range(3):
        #se todos os elementos da coluna 'i' forem iguais ao jogador tem 3 X ou 3 O na mesma linha, ou seja, jogador venceu
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True

    # CONFERE SE TEM VENCEDOR PELA DIAGONAL PRINCIPAL (\)
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    # CONFERE SE TEM VENCEDOR PELA VERIFICAR DIAGONAL SECUNDÁRIA (/)
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    #se chegou até aqui e não entrou em nenhum 'if' que retornou True, não houve vencedor
    return False


#Crie uma função para verificar se houve um empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro: #checa todas as linhas do tabuleiro
        if " " in linha: #se encontrar espaço vazio em alguma das linhas,
            return False #retorna falso porque não é empate, ainda há jogadas a serem feitas
    
    return True #se todos os espaços de todas as linhas estiverem preenchidos, então é um empate


#Crie uma função para verificar se uma jogada é válida
def jogada_valida(tabuleiro, linha, coluna): #recebe a matriz atualizada com o estado atual do jogo (tabuleiro) + o número da linha e coluna que o jogador escolheu
    if tabuleiro[linha][coluna] == " ": #compara a linha/coluna que o jogador com um espaço vazio
        return True #se a posição escolhida estiver vazia, retorna True = é uma jogada válida
    else:
        return False #se a posição escolhida não estiver vazia, retorna False = uma nova jogada é necessária


#Mostrar ranking
def mostrar_ranking(ranking):
    print("\nRANKING:")
    for jogador, pontos in ranking.items():
        print(f"{jogador}: {pontos} vitória(s)")
    print()


#Loop do jogo
def jogar():
    ranking = {} #cria o dicionário vazio que guarda as vitórias de cada jogador

    print("=== JOGO DA VELHA COM RANKING ===")

    jogador1_nome = input("Nome do Jogador 1: ")
    jogador2_nome = input("Nome do Jogador 2: ")

    jogador1 = input(f"{jogador1_nome}, escolha (X/O): ").upper() #se o jogador digitar x ou o minusculo, ele converte pra aceitar o valor também
    while jogador1 not in ["X", "O"]: #enquanto o jogador não digitar x ou o, a jogada não acontece
        jogador1 = input("Escolha inválida. Digite X ou O: ").upper()

    jogador2 = "O" if jogador1 == "X" else "X"

    ranking[jogador1_nome] = 0
    ranking[jogador2_nome] = 0

    while True:
        tabuleiro = criar_tabuleiro() #a cada partida, o tabuleiro é limpo (reiniciado)
        jogador_atual = jogador1 #controlam a vez
        nome_atual = jogador1_nome

        while True:
            exibir_tabuleiro(tabuleiro)
            print(f"Vez de {nome_atual} ({jogador_atual})")

            try:
                linha = int(input("Linha (0-2): "))
                coluna = int(input("Coluna (0-2): "))

                if linha not in range(3) or coluna not in range(3):
                    print("Posição inválida!") #se o jogador tentar jogar em uma posição fora das 3 linhas e 3 colunas
                    continue

                if not jogada_valida(tabuleiro, linha, coluna):
                    print("Posição ocupada!")
                    continue

                tabuleiro[linha][coluna] = jogador_atual

                if verificar_vencedor(tabuleiro, jogador_atual): #se identificar um vencedor, acaba a partida
                    exibir_tabuleiro(tabuleiro)
                    print(f"{nome_atual} venceu!")
                    ranking[nome_atual] += 1 #e adiciona um ponto na conta do vencedor da partida
                    break

                if verificar_empate(tabuleiro): #também acaba a partida se identificar um vencedor
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break

                # Trocar jogador
                if jogador_atual == jogador1: #se o jogador 1 fez a última jogada, ele "pula" a vez pro jogador 2 na joga seguinte
                    jogador_atual = jogador2
                    nome_atual = jogador2_nome
                else:
                    jogador_atual = jogador1 #else = se o jogador 2 foi o último a jogar, portanto agora é a vez do jogador 1
                    nome_atual = jogador1_nome

            except ValueError:
                print("Digite números válidos!")

        mostrar_ranking(ranking)

        continuar = input("Jogar novamente? (s/n): ").lower() #escolhe se quer jogar novamente ou não
        if continuar != "s":
            print("Fim do jogo!")
            break


#Execução
jogar()