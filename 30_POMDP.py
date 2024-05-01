# Importar la librería numpy para trabajar con matrices
import numpy as np

# Definir las acciones disponibles para el robot
actions = ['Move_Left', 'Move_Right', 'Move_Up', 'Move_Down']

# Definir las posiciones del laberinto y las observaciones posibles
states = ['S1', 'S2', 'S3', 'S4', 'S5']
observations = ['Left', 'Right']

# Definir las probabilidades de transición del estado
transition_probabilities = {
    'S1': {'Move_Left': {'S1': 0.8, 'S2': 0.2}, 'Move_Right': {'S2': 1.0}},
    'S2': {'Move_Left': {'S1': 0.5, 'S2': 0.5}, 'Move_Right': {'S3': 0.8, 'S2': 0.2}},
    'S3': {'Move_Left': {'S2': 0.8, 'S3': 0.2}, 'Move_Right': {'S4': 0.8, 'S3': 0.2}},
    'S4': {'Move_Left': {'S3': 0.8, 'S4': 0.2}, 'Move_Right': {'S5': 0.8, 'S4': 0.2}},
    'S5': {'Move_Left': {'S4': 0.8, 'S5': 0.2}}
}

# Definir las probabilidades de observación
observation_probabilities = {
    'S1': {'Left': {'S1': 0.8, 'S2': 0.2}, 'Right': {'S2': 1.0}},
    'S2': {'Left': {'S1': 0.5, 'S2': 0.5}, 'Right': {'S3': 0.8, 'S2': 0.2}},
    'S3': {'Left': {'S2': 0.8, 'S3': 0.2}, 'Right': {'S4': 0.8, 'S3': 0.2}},
    'S4': {'Left': {'S3': 0.8, 'S4': 0.2}, 'Right': {'S5': 0.8, 'S4': 0.2}},
    'S5': {'Left': {'S4': 0.8, 'S5': 0.2}}
}

# Definir las recompensas por estado
rewards = {'S5': 100, 'S1': -10, 'S2': -10, 'S3': -10, 'S4': -10}

# Definir la función de utilidad
def utility(state):
    return rewards.get(state, 0)

# Definir la función de utilidad observada
def observed_utility(state, observation):
    return rewards.get(state, 0) if observation == 'Right' else 0

# Definir la función de transición
def transition(state, action):
    return np.random.choice(list(transition_probabilities[state][action].keys()), 
                             p=list(transition_probabilities[state][action].values()))

# Definir la función de observación
def observe(state, action):
    return np.random.choice(list(observation_probabilities[state][action].keys()), 
                             p=list(observation_probabilities[state][action].values()))

# Implementar el algoritmo de búsqueda en profundidad (DFS) para encontrar la ruta óptima
def dfs(state, path):
    if state == 'S5':
        return path
    for action in actions:
        next_state = transition(state, action)
        path.append(action)
        observed = observe(next_state, action)
        if observed == 'Right':
            return dfs(next_state, path)
        path.pop()
    return path

# Ejecutar el algoritmo de búsqueda en profundidad (DFS) desde el estado inicial
initial_state = 'S1'
optimal_path = dfs(initial_state, [initial_state])
print("La ruta optima encontrada por el robot es:", optimal_path)
