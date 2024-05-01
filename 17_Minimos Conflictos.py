import random

def initial_state(n):
    """Genera un estado inicial aleatorio para el problema de las N reinas."""
    return [random.randint(0, n-1) for _ in range(n)]

def conflicts(state):
    """Calcula el número de conflictos en el estado actual."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def min_conflicts(state, max_steps=1000):
    """Resuelve el problema de las N reinas utilizando el algoritmo Min-Conflict."""
    n = len(state)
    for _ in range(max_steps):
        if conflicts(state) == 0:
            return state  # El estado actual es una solución
        # Selecciona una reina en conflicto y mueve a la posición con el mínimo conflicto
        queen = random.randint(0, n-1)
        min_conflict_value = float('inf')
        min_conflict_pos = state[queen]
        for pos in range(n):
            if pos != state[queen]:
                state[queen] = pos
                conflict_value = conflicts(state)
                if conflict_value < min_conflict_value:
                    min_conflict_value = conflict_value
                    min_conflict_pos = pos
        state[queen] = min_conflict_pos
    return None  # No se encontró una solución en el número máximo de pasos

# Resolvemos el problema de las 8 reinas utilizando Min-Conflict
n = 8
initial_state = initial_state(n)
solution = min_conflicts(initial_state)
if solution:
    print("Solucion encontrada:", solution)
else:
    print("No se encontró una solucion.")
