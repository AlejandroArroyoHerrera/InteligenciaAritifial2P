# Importar la librería numpy para trabajar con matrices
import numpy as np

# Definir las acciones y sus recompensas y probabilidades de transición
actions = {
    'Action_A': {'reward': 10, 'transition_probs': {'Action_A': 0.8, 'Action_B': 0.2}},
    'Action_B': {'reward': 20, 'transition_probs': {'Action_A': 0.5, 'Action_B': 0.5}}
}

# Definir la función de utilidad
def utility(state):
    if state == 'Goal':
        return 100
    else:
        return 0

# Definir el algoritmo de iteración de políticas
def policy_iteration_MDP():
    # Inicializar la política
    policy = {'State_A': 'Action_A', 'State_B': 'Action_B'}
    # Número máximo de iteraciones
    max_iterations = 100
    # Tasa de descuento
    gamma = 0.9

    # Iterar hasta que se alcance el número máximo de iteraciones o converja
    for _ in range(max_iterations):
        new_policy = {}
        for state in policy:
            action = policy[state]
            expected_value = actions[action]['reward'] + \
                             gamma * sum(actions[action]['transition_probs'][next_state] * utility(next_state) for next_state in actions[action]['transition_probs'])
            new_policy[state] = max(actions, key=lambda a: sum(actions[a]['transition_probs'][next_state] * utility(next_state) for next_state in actions[a]['transition_probs']))

        # Si la política no cambia, hemos convergido
        if new_policy == policy:
            break
        policy = new_policy

    return policy

# Ejecutar la iteración de políticas para el MDP
optimal_policy = policy_iteration_MDP()
print("La política optima es:", optimal_policy)
