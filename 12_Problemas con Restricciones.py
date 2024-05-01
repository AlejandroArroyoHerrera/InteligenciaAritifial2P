from constraint import Problem

# Creamos una instancia del problema de satisfacción de restricciones
problem = Problem()

# Definimos las variables del problema, que son los nodos del grafo
nodes = ['A', 'B', 'C', 'D']

# Añadimos las variables al problema, asignando el dominio de colores (rojo, verde, azul)
for node in nodes:
    problem.addVariable(node, ['rojo', 'verde', 'azul'])

# Añadimos las restricciones al problema, que garantizan que no haya nodos adyacentes con el mismo color
problem.addConstraint(lambda x, y: x != y, ('A', 'B'))
problem.addConstraint(lambda x, y: x != y, ('A', 'C'))
problem.addConstraint(lambda x, y: x != y, ('B', 'C'))
problem.addConstraint(lambda x, y: x != y, ('B', 'D'))

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)
