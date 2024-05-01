import numpy as np

# Definir el conjunto de datos de juegos previos (estado, acción, recompensa)
data = [
    ((0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0),
    ((0, 0, 0, 0, 0, 0, 0, 0, 1), 1, -1),
    ((0, 0, 0, 0, 0, 0, 0, 0, 1), 3, 1),
    # Más ejemplos de juegos previos...
]

# Inicializar la tabla Q
Q = np.zeros((9, 9))

# Actualizar la tabla Q con los ejemplos de juegos previos
for state, action, reward in data:
    Q[state, action] = reward

# Mostrar la tabla Q actualizada
print("Tabla Q actualizada:")
print(Q)
