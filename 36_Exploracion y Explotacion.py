import numpy as np

# Definir una función para la selección de acción con ε-Greedy
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        # Exploración: seleccionar una acción aleatoria
        return np.random.choice(len(Q[state]))
    else:
        # Explotación: seleccionar la mejor acción conocida
        return np.argmax(Q[state])

# Ejemplo de uso:
Q = [[0.5, 0.2, 0.1], [0.3, 0.4, 0.9]]  # Valores Q para dos estados y tres acciones
state = 0
epsilon = 0.1  # Probabilidad de exploración
action = epsilon_greedy(Q, state, epsilon)
print("Acción seleccionada:", action)
