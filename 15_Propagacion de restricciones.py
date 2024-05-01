from constraint import Problem, AllDifferentConstraint

# Creamos una instancia del problema de satisfacción de restricciones
problem = Problem()

# Definimos las variables del problema, que son las columnas del tablero (del 0 al N-1)
columns = range(8)

# Añadimos las variables al problema, asignando el dominio de filas (del 0 al N-1)
for col in columns:
    problem.addVariable(col, columns)

# Añadimos las restricciones al problema para garantizar que no haya dos reinas en la misma fila ni en la misma diagonal
for col1 in columns:
    for col2 in columns:
        if col1 < col2:
            # Restricción para evitar dos reinas en la misma fila
            problem.addConstraint(lambda row1, row2, c1=col1, c2=col2: row1 != row2, (col1, col2))
            # Restricción para evitar dos reinas en la misma diagonal
            problem.addConstraint(lambda row1, row2, c1=col1, c2=col2: abs(row1 - row2) != abs(c1 - c2), (col1, col2))

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)
