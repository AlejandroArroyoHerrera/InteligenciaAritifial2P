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

# Función de evaluación para el juego del Gato
def evaluate(board):
    _, winner = game_over(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    else:
        return 0

# Función Minimax con corte de búsqueda por efecto horizonte
def minimax_with_horizon(board, depth, maximizing_player):
    if depth == 0 or game_over(board)[0]:
        return evaluate(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval = minimax_with_horizon(board, depth - 1, False)
                    board[i][j] = '-'
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval = minimax_with_horizon(board, depth - 1, True)
                    board[i][j] = '-'
                    min_eval = min(min_eval, eval)
        return min_eval

# Función para encontrar la mejor jugada utilizando Minimax con corte de búsqueda por efecto horizonte
def find_best_move_with_horizon(board, depth):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                eval = minimax_with_horizon(board, depth - 1, False)
                board[i][j] = '-'
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Simulamos el juego del Gato utilizando Minimax con corte de búsqueda por efecto horizonte
while not game_over(board)[0]:
    print_board(board)
    player_move = input("Ingresa tu movimiento (fila,columna): ")
    row, col = map(int, player_move.split(','))
    board[row][col] = 'X'
    if game_over(board)[0]:
        break
    print("Turno de la IA...")
    ai_move = find_best_move_with_horizon(board, depth=2)
    board[ai_move[0]][ai_move[1]] = 'O'

print_board(board)
winner = game_over(board)[1]
if winner:
    print(f"Ganador: {winner}")
else:
    print("Empate")
