import random

def tabu_search(graph, start, goal, tabu_size=5, max_iterations=100):
    # Inicializamos la lista tabú vacía
    tabu_list = []
    # Inicializamos el nodo actual como el nodo inicial
    current_node = start
    # Inicializamos el mejor camino encontrado hasta ahora como el camino directo entre el nodo inicial y el objetivo
    best_path = [start, goal]
    
    # Iteramos hasta alcanzar el número máximo de iteraciones
    for _ in range(max_iterations):
        # Generamos una lista de vecinos del nodo actual
        neighbors = graph[current_node]
        # Seleccionamos aleatoriamente un vecino que no esté en la lista tabú
        non_tabu_neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]
        if not non_tabu_neighbors:
            # Si no hay vecinos no tabú, salimos del bucle
            break
        next_node = random.choice(non_tabu_neighbors)
        
        # Actualizamos la lista tabú y el nodo actual
        tabu_list.append(next_node)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        current_node = next_node
        
        # Si encontramos un camino mejor al objetivo, lo actualizamos
        if current_node == goal:
            best_path = [start] + tabu_list + [goal]
    
    return best_path

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
tabu_size = 3
max_iterations = 100

best_path = tabu_search(graph, start_node, goal_node, tabu_size, max_iterations)
print("Mejor camino encontrado:", best_path)
