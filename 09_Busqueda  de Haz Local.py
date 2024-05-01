import random

def beam_search(graph, start, goal, beam_width=2, max_iterations=100):
    # Inicializamos el haz como una lista que contiene solo el nodo inicial
    beam = [[start]]
    
    # Iteramos hasta alcanzar el número máximo de iteraciones
    for _ in range(max_iterations):
        # Creamos un nuevo haz vacío
        new_beam = []
        # Expandimos cada camino en el haz actual
        for path in beam:
            # Obtenemos el último nodo en el camino
            current_node = path[-1]
            # Si hemos alcanzado el nodo objetivo, retornamos el camino encontrado
            if current_node == goal:
                return path
            # Expandimos el camino agregando los vecinos del último nodo
            neighbors = graph[current_node]
            for neighbor in neighbors:
                new_path = path + [neighbor]
                new_beam.append(new_path)
        # Seleccionamos los mejores caminos para formar el nuevo haz
        beam = sorted(new_beam, key=lambda x: heuristic(x[-1], goal))[:beam_width]
    
    # Si no se encuentra un camino al objetivo dentro del límite de iteraciones, retornamos None
    return None

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
goal_node = 'F'
beam_width = 2
max_iterations = 100

best_path = beam_search(graph, start_node, goal_node, beam_width, max_iterations)
print("Mejor camino encontrado:", best_path)
