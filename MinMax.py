import math

# Define as constantes para o jogo da velha
X = "X"
O = "O"
EMPTY = None

# Define a função para avaliar o estado atual do tabuleiro
def evaluate(board):
    # Verifica todas as linhas, colunas e diagonais para determinar se algum jogador ganhou
    for player in [X, O]:
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player) or \
           any(all(board[i][j] == player for j in range(3)) for i in range(3)) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)):
            return 1 if player == X else -1

    # Se ninguém ganhou, retorna 0
    return 0

# Define a função para verificar se o jogo terminou
def game_over(board):
    # Verifica se algum jogador ganhou
    if evaluate(board) != 0:
        return True

    # Verifica se o tabuleiro está cheio
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True

# Define a função para obter todas as jogadas possíveis
def get_moves(board, player):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                new_board = [[board[row][col] for col in range(3)] for row in range(3)]
                new_board[i][j] = player
                moves.append((new_board, (i, j)))

    return moves

# Define a função para aplicar o algoritmo Minimax
def minimax(board, player):
    # Verifica se o jogo terminou
    if game_over(board):
        return evaluate(board), None

    # Obtém todas as jogadas possíveis
    moves = get_moves(board, player)

    # Aplica o algoritmo Minimax para cada jogada possível
    if player == X:
        best_score = -math.inf
        for move, _ in moves:
            score, _ = minimax(move, O)
            if score > best_score:
                best_score = score
                best_move = move
    else:
        best_score = math.inf
        for move, _ in moves:
            score, _ = minimax(move, X)
            if score < best_score:
                best_score = score
                best_move = move

    return best_score, best_move

# Define a função para exibir o tabuleiro
def display_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j] if board[i][j] is not None else ".", end=" ")
        print()

# Inicia o jogo
board = [[EMPTY for _ in range(3)] for _ in range(3)]
display_board(board)

# Loop principal do jogo
while not game_over(board):
    # Obtém a jogada do jogador
    row = int(input("Digite a linha da sua jogada (0 a 2): "))
    col = int(input("Digite a coluna da suajogada (0 a 2): "))
    while board[row][col] is not EMPTY:
        print("Essa posição já está ocupada, tente novamente.")
        row = int(input("Digite a linha da sua jogada (0 a 2): "))
        col = int(input("Digite a coluna da sua jogada (0 a 2): "))
    board[row][col] = X
    display_board(board)

    # Verifica se o jogo terminou após a jogada do jogador
    if game_over(board):
        break

    # Obtém a jogada do computador
    _, move = minimax(board, O)
    board = move
    display_board(board)

# Exibe o resultado do jogo
result = evaluate(board)
if result == 1:
    print("Você perdeu!")
elif result == -1:
    print("Você ganhou!")
else:
    print("Empate!")