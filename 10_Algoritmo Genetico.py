import random

def create_individual(graph, start, goal):
    # Genera un camino aleatorio desde el nodo inicial al objetivo
    individual = [start]
    current_node = start
    while current_node != goal:
        neighbors = graph[current_node]
        next_node = random.choice(neighbors)
        individual.append(next_node)
        current_node = next_node
    return individual

def crossover(parent1, parent2):
    # Realiza un cruce en un punto entre dos padres para generar un hijo
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, graph, start, goal, mutation_rate=0.1):
    # Realiza una mutación en un individuo con una tasa dada
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            # Reemplaza un nodo en el camino con un nodo aleatorio del grafo, excepto el nodo inicial y el objetivo
            if i == 0:
                individual[i] = start
            elif i == len(individual) - 1:
                individual[i] = goal
            else:
                individual[i] = random.choice(list(graph.keys()))
    return individual

def fitness(individual, graph, start, goal):
    # Calcula la aptitud de un individuo como la inversa de la distancia entre el objetivo y el último nodo del camino
    distance_to_goal = len(individual) - 1
    return 1 / distance_to_goal

def genetic_algorithm(graph, start, goal, population_size=50, crossover_rate=0.8, mutation_rate=0.1, generations=100):
    # Inicializa una población de individuos aleatorios
    population = [create_individual(graph, start, goal) for _ in range(population_size)]
    
    # Evoluciona la población durante un número fijo de generaciones
    for _ in range(generations):
        # Evalúa la aptitud de cada individuo en la población
        fitness_scores = [fitness(individual, graph, start, goal) for individual in population]
        
        # Selecciona a los padres para la reproducción utilizando selección por ruleta
        parents = random.choices(population, weights=fitness_scores, k=population_size)
        
        # Crea la siguiente generación de individuos mediante el cruce y la mutación
        next_generation = []
        for i in range(0, population_size, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            if random.random() < crossover_rate:
                child1 = crossover(parent1, parent2)
                child2 = crossover(parent2, parent1)
            else:
                child1 = parent1
                child2 = parent2
            child1 = mutate(child1, graph, start, goal, mutation_rate)
            child2 = mutate(child2, graph, start, goal, mutation_rate)
            next_generation.extend([child1, child2])
        
        # Reemplaza la población actual con la siguiente generación
        population = next_generation
    
    # Devuelve el mejor individuo de la última generación
    best_individual = max(population, key=lambda x: fitness(x, graph, start, goal))
    return best_individual

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
population_size = 50
crossover_rate = 0.8
mutation_rate = 0.1
generations = 100

best_path = genetic_algorithm(graph, start_node, goal_node, population_size, crossover_rate, mutation_rate, generations)
print("Mejor camino encontrado:", best_path)
