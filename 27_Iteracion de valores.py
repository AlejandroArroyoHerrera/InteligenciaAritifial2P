# Función para imprimir el tablero del Gato
def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

# Función para verificar si hay un ganador o si el tablero está lleno
def game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-' or board[0][i] == board[1][i] == board[2][i] != '-':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '-' or board[0][2] == board[1][1] == board[2][0] != '-':
        return True
    if all(board[i][j] != '-' for i in range(3) for j in range(3)):
        return True
    return False

# Función para calcular la utilidad de un estado del tablero para el jugador dado
def utility(board, player):
    if player == 'O':
        opponent = 'X'
    else:
        opponent = 'O'
    
    if game_over(board):
        if player == 'O':
            return -1 if game_over(board) else 0
        else:
            return 1 if game_over(board) else 0

    # Supongamos una función de utilidad simple basada en la cantidad de filas, columnas y diagonales ganadoras
    utility_value = 0
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or \
           board[0][i] == board[1][i] == board[2][i] == player:
            utility_value += 1
        if board[i][0] == board[i][1] == board[i][2] == opponent or \
           board[0][i] == board[1][i] == board[2][i] == opponent:
            utility_value -= 1
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        utility_value += 1
    if board[0][0] == board[1][1] == board[2][2] == opponent or \
       board[0][2] == board[1][1] == board[2][0] == opponent:
        utility_value -= 1
    
    return utility_value

# Función para realizar la iteración de valores en el juego del Gato
def value_iteration_tictactoe():
    # Inicializar el tablero
    board = [['-' for _ in range(3)] for _ in range(3)]
    # Diccionario para almacenar los valores de los estados
    values = {}
    # Número máximo de iteraciones
    max_iterations = 1000
    # Tasa de descuento
    gamma = 0.9
    
    # Iterar hasta que se alcance el número máximo de iteraciones o converja
    for _ in range(max_iterations):
        delta = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    original_value = values.get(str(board), 0)
                    # Calcular el valor de este estado como la utilidad máxima posible para el jugador 'O'
                    values[str(board)] = max(values.get(str(board), 0), utility(board, 'O'))
                    delta = max(delta, abs(original_value - values.get(str(board), 0)))
    
    # Una vez que la iteración haya convergido, seleccionamos la mejor acción posible para 'O'
    best_move = None
    best_value = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-' and utility(board, 'O') > best_value:
                best_move = (i, j)
                best_value = utility(board, 'O')

    return best_move

# Ejecutar la iteración de valores para el juego del Gato
best_move = value_iteration_tictactoe()
print("La mejor jugada para el jugador 'O' es:", best_move)
