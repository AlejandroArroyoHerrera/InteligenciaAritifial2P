import math

# Definimos el tablero del juego del Gato
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

# Función para verificar si hay un ganador o si el tablero está lleno
def game_over(board):
    # Verifica filas y columnas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-' or board[0][i] == board[1][i] == board[2][i] != '-':
            return True, board[i][0]
    # Verifica diagonales
    if board[0][0] == board[1][1] == board[2][2] != '-' or board[0][2] == board[1][1] == board[2][0] != '-':
        return True, board[1][1]
    # Verifica si el tablero está lleno
    if all(board[i][j] != '-' for i in range(3) for j in range(3)):
        return True, None
    return False, None

# Función para evaluar la utilidad del tablero para el jugador dado
def evaluate(board, player):
    _, winner = game_over(board)
    if winner == player:
        return 1
    elif winner is None:
        return 0
    else:
        return -1

# Función Minimax con posibilidad Minimax Esperado
def expected_minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board)[0]:
        return evaluate(board, 'O')
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval = expected_minimax(board, depth - 1, False)
                    board[i][j] = '-'
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval = expected_minimax(board, depth - 1, True)
                    board[i][j] = '-'
                    min_eval = min(min_eval, eval)
        return min_eval

# Función para encontrar la mejor jugada utilizando Minimax con posibilidad Minimax Esperado
def find_best_move_expected_minimax(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                eval = expected_minimax(board, 9, False)
                board[i][j] = '-'
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Simulamos el juego del Gato utilizando Minimax con posibilidad Minimax Esperado
while not game_over(board)[0]:
    print_board(board)
    player_move = input("Ingresa tu movimiento (fila,columna): ")
    row, col = map(int, player_move.split(','))
    board[row][col] = 'X'
    if game_over(board)[0]:
        break
    print("Turno de la IA...")
    ai_move = find_best_move_expected_minimax(board)
    board[ai_move[0]][ai_move[1]] = 'O'

print_board(board)
winner = game_over(board)[1]
if winner:
    print(f"Ganador: {winner}")
else:
    print("Empate")
