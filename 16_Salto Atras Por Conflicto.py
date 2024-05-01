from constraint import Problem, BacktrackingSolver

# Creamos una instancia del problema de satisfacción de restricciones
problem = Problem(BacktrackingSolver())

# Definimos una función para verificar si es seguro colocar una reina en una posición determinada
def is_safe(queens, row, col):
    for q_row, q_col in enumerate(queens):
        if q_col == col or abs(q_row - row) == abs(q_col - col):
            return False
    return True

# Función recursiva para colocar las reinas en el tablero
def place_queens(queens, n):
    if len(queens) == n:  # Si todas las reinas están colocadas, retornamos el tablero
        return queens
    for col in range(n):
        if is_safe(queens, len(queens), col):
            queens.append(col)
            result = place_queens(queens, n)
            if result is not None:  # Si encontramos una solución, la retornamos
                return result
            queens.pop()  # Si no encontramos una solución, retrocedemos y probamos en la siguiente columna
    return None

# Resolvemos el problema
n = 8  # Por ejemplo, para el problema de las 8 reinas
queens = place_queens([], n)

# Imprimimos el tablero con las reinas colocadas
if queens is not None:
    for row, col in enumerate(queens):
        print('.' * col + 'Q' + '.' * (n - col - 1))
else:
    print("No se encontro ninguna solucion.")
