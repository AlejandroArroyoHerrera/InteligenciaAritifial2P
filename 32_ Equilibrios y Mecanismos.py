# Importar la librería nashpy para trabajar con teoría de juegos
import nashpy as nash

# Definir las matrices de pagos para ambos jugadores
prisoner_A = [[3, 0], [5, 1]]
prisoner_B = [[3, 5], [0, 1]]

# Crear el juego utilizando las matrices de pagos
game = nash.Game(prisoner_A, prisoner_B)

# Encontrar el equilibrio de Nash
equilibria = game.support_enumeration()

print("Equilibrio(s) de Nash encontrados:")
for eq in equilibria:
    print("Jugador A:", eq[0], ", Jugador B:", eq[1])
