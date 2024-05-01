import heapq

def heuristic(node, goal):
    # Función heurística, en este caso, la distancia heurística estimada desde el nodo hasta el objetivo
    return 0  # En este ejemplo, no utilizaremos una heurística, por lo que devolvemos cero

def astar_search_online(graph, start, goal):
    # Inicializamos la lista de nodos por explorar con el nodo inicial
    frontier = [(0, start)]  # Tuplas (f, nodo), donde f es la suma del costo real y la heurística estimada
    explored = set()  # Conjunto de nodos explorados
    
    # Mientras haya nodos por explorar
    while frontier:
        # Extraemos el nodo de la frontera con el menor valor de f
        _, current_node = heapq.heappop(frontier)
        
        # Si encontramos el objetivo, retornamos el camino
        if current_node == goal:
            return True  # En una búsqueda online, podemos devolver True cuando encontramos el objetivo
        
        # Exploramos los vecinos del nodo actual
        for neighbor in graph[current_node]:
            if neighbor not in explored:
                # Agregamos el vecino a la frontera con su valor de f
                heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor))
                # Marcamos el vecino como explorado
                explored.add(neighbor)
    
    # Si no encontramos el objetivo, retornamos False
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

if astar_search_online(graph, start_node, goal_node):
    print("Se encontro el objetivo.")
else:
    print("No se encontro el objetivo.")
