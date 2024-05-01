import random
import math

def simulated_annealing(graph, start, goal, initial_temperature=100, cooling_rate=0.95, max_iterations=1000):
    # Inicializamos el nodo actual como el nodo inicial
    current_node = start
    # Inicializamos la temperatura inicial
    temperature = initial_temperature
    
    # Iteramos hasta alcanzar el número máximo de iteraciones o hasta que la temperatura sea muy baja
    for _ in range(max_iterations):
        # Si hemos alcanzado el nodo objetivo, retornamos el camino encontrado
        if current_node == goal:
            return True
        
        # Obtenemos los vecinos del nodo actual
        neighbors = graph[current_node]
        # Seleccionamos aleatoriamente un vecino
        next_node = random.choice(neighbors)
        
        # Calculamos la diferencia en el costo entre el vecino y el nodo actual
        delta_cost = 1  # Consideramos que el costo de cualquier movimiento es 1
        
        # Si el movimiento es favorable (menor costo) o es aceptado con una probabilidad dada por la temperatura
        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_node = next_node
        
        # Disminuimos la temperatura según el enfriamiento exponencial
        temperature *= cooling_rate
    
    # Si no se encuentra un camino al objetivo dentro del límite de iteraciones, retornamos False
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
initial_temperature = 100
cooling_rate = 0.95
max_iterations = 1000

found_path = simulated_annealing(graph, start_node, goal_node, initial_temperature, cooling_rate, max_iterations)
if found_path:
    print("Se encontro un camino al nodo objetivo.")
else:
    print("No se encontro un camino al nodo objetivo.")
