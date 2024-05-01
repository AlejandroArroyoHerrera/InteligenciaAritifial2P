def bidirectional_bfs(graph, start, goal):
    # Creamos una cola para la búsqueda desde el nodo inicial
    queue_start = deque([start])
    # Creamos un conjunto para mantener un registro de los nodos visitados desde el nodo inicial
    visited_start = set()
    visited_start.add(start)
    # Creamos un diccionario para almacenar los padres de los nodos visitados desde el nodo inicial
    parent_start = {start: None}
    
    # Creamos una cola para la búsqueda desde el nodo objetivo
    queue_goal = deque([goal])
    # Creamos un conjunto para mantener un registro de los nodos visitados desde el nodo objetivo
    visited_goal = set()
    visited_goal.add(goal)
    # Creamos un diccionario para almacenar los padres de los nodos visitados desde el nodo objetivo
    parent_goal = {goal: None}
    
    # Mientras haya nodos en ambas colas
    while queue_start and queue_goal:
        # Realizamos una iteración desde el nodo inicial
        current_start = queue_start.popleft()
        # Verificamos si el nodo actual está en el conjunto de nodos visitados desde el nodo objetivo
        if current_start in visited_goal:
            # Construimos el camino desde el nodo inicial hasta el nodo objetivo
            path = []
            while current_start is not None:
                path.append(current_start)
                current_start = parent_start[current_start]
            current_goal = goal
            while current_goal is not None:
                path.append(current_goal)
                current_goal = parent_goal[current_goal]
            return path[::-1]
        # Para cada vecino del nodo actual en el grafo desde el nodo inicial
        for neighbor in graph[current_start]:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                parent_start[neighbor] = current_start
                queue_start.append(neighbor)
        
        # Realizamos una iteración desde el nodo objetivo
        current_goal = queue_goal.popleft()
        # Verificamos si el nodo actual está en el conjunto de nodos visitados desde el nodo inicial
        if current_goal in visited_start:
            # Construimos el camino desde el nodo inicial hasta el nodo objetivo
            path = []
            while current_goal is not None:
                path.append(current_goal)
                current_goal = parent_goal[current_goal]
            current_start = start
            while current_start is not None:
                path.append(current_start)
                current_start = parent_start[current_start]
            return path
        
        # Para cada vecino del nodo actual en el grafo desde el nodo objetivo
        for neighbor in graph[current_goal]:
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                parent_goal[neighbor] = current_goal
                queue_goal.append(neighbor)
    
    # Si no se puede encontrar un camino entre el nodo inicial y el nodo objetivo
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
print("Camino encontrado:", bidirectional_bfs(graph, start_node, goal_node))
