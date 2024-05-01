#N reinas
def is_valid(board, row, col):
    # Verifica si es seguro colocar una reina en la posición (row, col)
    # Comprueba si hay una reina en la misma columna
    for i in range(row):
        if board[i] == col:
            return False
        # Comprueba diagonales
        if abs(i - row) == abs(board[i] - col):
            return False
    return True

def backtracking_n_queens(board, row, n):
    # Si todas las reinas están colocadas, retorna verdadero
    if row == n:
        return True
    # Intenta colocar una reina en cada columna de la fila actual
    for col in range(n):
        if is_valid(board, row, col):
            # Si es seguro colocar una reina en esta posición, la colocamos y continuamos con la siguiente fila
            board[row] = col
            if backtracking_n_queens(board, row + 1, n):
                return True
            # Si no es posible colocar una reina en la siguiente fila con esta configuración, retrocedemos
            board[row] = -1
    # Si no se puede colocar ninguna reina en esta fila, retornamos falso
    return False

def solve_n_queens(n):
    board = [-1] * n  # Inicializamos el tablero vacío
    if backtracking_n_queens(board, 0, n):
        # Si se encontró una solución, imprimimos el tablero
        for i in range(n):
            print('.' * board[i] + 'Q' + '.' * (n - board[i] - 1))
    else:
        print("No hay solucion para el problema de las N reinas.")

# Ejemplo de uso
n = 8  # Por ejemplo, para el problema de las 8 reinas
solve_n_queens(n)
