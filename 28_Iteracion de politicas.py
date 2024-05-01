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

# Función para realizar la iteración de políticas en el juego del Gato
def policy_iteration_tictactoe():
    # Inicializar la política
    policy = {(i, j): '-' for i in range(3) for j in range(3)}
    # Número máximo de iteraciones
    max_iterations = 1000
    # Tasa de descuento
    gamma = 0.9
    
    # Iterar hasta que se alcance el número máximo de iteraciones o converja
    for _ in range(max_iterations):
        # Evaluación de la política
        values = {}
        for i in range(3):
            for j in range(3):
                if policy[(i, j)] == '-':
                    board = [row[:] for row in policy.values()]
                    board[i][j] = 'O'
                    values[(i, j)] = utility(board, 'O')
        # Mejora de la política
        for i in range(3):
            for j in range(3):
                if policy[(i, j)] == '-' and values[(i, j)] == max(values.values()):
                    policy[(i, j)] = 'O'
    
    return policy

# Ejecutar la iteración de políticas para el juego del Gato
optimal_policy = policy_iteration_tictactoe()
print("La política optima para el jugador 'O' es:")
print_board([[optimal_policy[(i, j)] for j in range(3)] for i in range(3)])
