import random

# Exibe o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print()
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print()

# Verifica se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    vitoria_condicoes = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
                         (0, 4, 8), (2, 4, 6)]             # Diagonais
    for condicao in vitoria_condicoes:
        if tabuleiro[condicao[0]] == tabuleiro[condicao[1]] == tabuleiro[condicao[2]] == jogador:
            return True
    return False

# Verifica se houve empate
def verificar_empate(tabuleiro):
    return " " not in tabuleiro

# Função do movimento do jogador humano
def movimento_jogador(tabuleiro):
    while True:
        posicao = input("Escolha uma posição (1-9): ")
        if posicao.isdigit() and int(posicao) in range(1, 10):
            posicao = int(posicao) - 1
            if tabuleiro[posicao] == " ":
                tabuleiro[posicao] = "X"
                break
            else:
                print("Parece que essa posição já está ocupada, tente outra. :)")
        else:
            print("Apenas números entre 1 e 9, por favor!")

# Função que calcula o movimento da IA usando o algoritmo Minimax
def minimax(tabuleiro, profundidade, is_maximizador):
    if verificar_vencedor(tabuleiro, "O"):
        return 1
    elif verificar_vencedor(tabuleiro, "X"):
        return -1
    elif verificar_empate(tabuleiro):
        return 0

    if is_maximizador:
        melhor_pontuacao = -float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                pontuacao = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = " "
                melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                pontuacao = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = " "
                melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

# Movimento da IA com base na dificuldade
def movimento_ia(tabuleiro, dificuldade):
    if dificuldade == "muito fácil":
        movimento_aleatorio(tabuleiro)
    elif dificuldade == "fácil":
        if random.random() > 0.5:
            movimento_aleatorio(tabuleiro)  # 50% de chance de movimento aleatório
        else:
            melhor_movimento_minimax(tabuleiro, 0)  # IA tenta fazer um movimento inteligente
    elif dificuldade == "intermediário":
        melhor_movimento_minimax(tabuleiro, 2)  # Limita a profundidade do Minimax
    elif dificuldade == "difícil":
        melhor_movimento_minimax(tabuleiro, 4)  # IA joga mais profundamente
    elif dificuldade == "muito difícil":
        melhor_movimento_minimax(tabuleiro, float("inf"))  # Minimax completo

# Função que faz o movimento aleatório
def movimento_aleatorio(tabuleiro):
    movimentos_disponiveis = [i for i in range(9) if tabuleiro[i] == " "]
    movimento = random.choice(movimentos_disponiveis)
    tabuleiro[movimento] = "O"

# Função que faz o melhor movimento usando o Minimax
def melhor_movimento_minimax(tabuleiro, profundidade_max):
    melhor_pontuacao = -float("inf")
    melhor_movimento = None
    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = i
    if melhor_movimento is not None:
        tabuleiro[melhor_movimento] = "O"

# Função para reiniciar o jogo
def reiniciar_jogo():
    while True:
        resposta = input("Vamos mais uma? :) (s/n): ").lower()
        if resposta == "s":
            return True
        elif resposta == "n":
            print("OK! Estarei aqui para uma futura revanche :)")
            return False
        else:
            print("Resposta inválida :(  Tente 's' ou 'n'")

# Função para escolher a dificuldade
def escolher_dificuldade():
    while True:
        print("Escolha o nível de dificuldade:")
        print("1. Muito fácil")
        print("2. Fácil")
        print("3. Intermediário")
        print("4. Difícil")
        print("5. Muito difícil")
        escolha = input("Digite o número correspondente: ")
        if escolha == "1":
            return "muito fácil"
        elif escolha == "2":
            return "fácil"
        elif escolha == "3":
            return "intermediário"
        elif escolha == "4":
            return "difícil"
        elif escolha == "5":
            return "muito difícil"
        else:
            print("Escolha inválida. Tente novamente.")

# Função principal do jogo
def jogo():
    while True:
        dificuldade = escolher_dificuldade()
        tabuleiro = [" " for _ in range(9)]
        print("Bem-vindo ao Jogo da Velha! Preparado?")
        exibir_tabuleiro(tabuleiro)

        while True:
            # Movimento do jogador humano
            movimento_jogador(tabuleiro)
            exibir_tabuleiro(tabuleiro)
            if verificar_vencedor(tabuleiro, "X"):
                print("Aeeee, você ganhou :P")
                break
            if verificar_empate(tabuleiro):
                print("Empatee! :0")
                break

            # Movimento da IA
            movimento_ia(tabuleiro, dificuldade)
            exibir_tabuleiro(tabuleiro)
            if verificar_vencedor(tabuleiro, "O"):
                print("A IA venceu! :(")
                break
            if verificar_empate(tabuleiro):
                print("Empatee! :0")
                break

        # Pergunta se o jogador quer reiniciar
        if not reiniciar_jogo():
            break

# Inicia o jogo
if __name__ == "__main__":
    jogo()
