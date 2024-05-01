import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    # Creamos una cola de prioridad para almacenar los nodos que estamos explorando
    queue = [(heuristic(start, goal), start)]
    # Creamos un conjunto para mantener un registro de los nodos ya visitados
    visited = set()
    
    # Mientras haya nodos en la cola
    while queue:
        # Sacamos el nodo con la heurística más baja de la cola
        _, current_node = heapq.heappop(queue)
        # Si el nodo actual es el objetivo, retornamos el camino
        if current_node == goal:
            return True
        
        # Marcamos el nodo actual como visitado
        visited.add(current_node)
        
        # Para cada vecino del nodo actual
        for neighbor in graph[current_node]:
            # Si el vecino no ha sido visitado
            if neighbor not in visited:
                # Calculamos la heurística del vecino
                h = heuristic(neighbor, goal)
                # Añadimos el vecino a la cola de prioridad con su heurística como prioridad
                heapq.heappush(queue, (h, neighbor))
    
    # Si no se encuentra un camino al objetivo, retornamos False
    return False

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

# Definimos una heurística simple basada en la distancia entre nodos
def heuristic(node, goal):
    distances = {
        'A': 3,
        'B': 2,
        'C': 2,
        'D': 1,
        'E': 1,
        'F': 0
    }
    return distances[node]

print("Hay un camino al nodo objetivo?", greedy_best_first_search(graph, start_node, goal_node, heuristic))
