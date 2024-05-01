import heapq

def a_star_search(graph, start, goal, heuristic, cost_func):
    # Creamos una cola de prioridad para almacenar los nodos que estamos explorando
    queue = [(0 + heuristic(start, goal), 0, start)]
    # Creamos un conjunto para mantener un registro de los nodos ya visitados
    visited = set()
    # Creamos un diccionario para almacenar los costos mínimos conocidos para llegar a cada nodo
    costs = {start: 0}
    # Creamos un diccionario para almacenar los padres de los nodos en el camino óptimo
    parents = {start: None}
    
    # Mientras haya nodos en la cola
    while queue:
        # Sacamos el nodo con el menor costo total de la cola
        _, current_cost, current_node = heapq.heappop(queue)
        # Si el nodo actual es el objetivo, reconstruimos y retornamos el camino óptimo
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]
        
        # Si el nodo actual no ha sido visitado
        if current_node not in visited:
            # Marcamos el nodo actual como visitado
            visited.add(current_node)
            # Para cada vecino del nodo actual
            for neighbor in graph[current_node]:
                # Calculamos el costo del nodo vecino desde el nodo inicial
                new_cost = current_cost + cost_func(current_node, neighbor)
                # Si el nodo vecino no ha sido visitado o el nuevo costo es menor que el costo previamente conocido
                if neighbor not in costs or new_cost < costs[neighbor]:
                    # Actualizamos el costo mínimo conocido para llegar al nodo vecino
                    costs[neighbor] = new_cost
                    # Calculamos la heurística del nodo vecino
                    h = new_cost + heuristic(neighbor, goal)
                    # Añadimos el nodo vecino a la cola de prioridad con su costo total como prioridad
                    heapq.heappush(queue, (h, new_cost, neighbor))
                    # Guardamos el nodo actual como padre del nodo vecino en el camino óptimo
                    parents[neighbor] = current_node
    
    # Si no se encuentra un camino al objetivo, retornamos None
    return None

# Ejemplo de uso
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 4, 'E': 7},
    'C': {'A': 3, 'F': 6},
    'D': {'B': 4},
    'E': {'B': 7, 'F': 8},
    'F': {'C': 6, 'E': 8}
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

# Definimos una función de costo simple basada en los pesos de los bordes
def cost_func(node1, node2):
    return graph[node1][node2]

print("Camino encontrado:", a_star_search(graph, start_node, goal_node, heuristic, cost_func))
