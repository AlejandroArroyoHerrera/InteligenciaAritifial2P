# Definimos el tablero del juego del Gato
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

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
        # Contamos cuántas filas, columnas y diagonales ha completado cada jugador
        player_o_score = player_x_score = 0
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == 'O' or board[0][i] == board[1][i] == board[2][i] == 'O':
                player_o_score += 1
            if board[i][0] == board[i][1] == board[i][2] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'X':
                player_x_score += 1
        if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
            player_o_score += 1
        if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
            player_x_score += 1
        return player_o_score - player_x_score

# Ejemplo de uso de la función de evaluación
board = [['X', '-', '-'], ['O', 'O', '-'], ['-', '-', 'X']]
print("Puntuacion de la posición del tablero:", evaluate(board))
