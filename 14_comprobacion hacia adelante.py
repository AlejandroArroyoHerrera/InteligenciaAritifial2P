from constraint import Problem, AllDifferentConstraint

# Creamos una instancia del problema de satisfacción de restricciones
problem = Problem()

# Definimos las variables del problema, que son los nodos del grafo
nodes = ['A', 'B', 'C', 'D']

# Añadimos las variables al problema, asignando el dominio de colores (rojo, verde, azul)
for node in nodes:
    problem.addVariable(node, ['rojo', 'verde', 'azul'])

# Añadimos la restricción de que ningún par de nodos adyacentes tenga el mismo color
problem.addConstraint(AllDifferentConstraint(), nodes)

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)
