# Matriz de pago para el dilema del prisionero:
#   - Si ambos jugadores cooperan, reciben una recompensa moderada.
#   - Si un jugador traiciona mientras el otro coopera, el traidor recibe una recompensa alta y el cooperador recibe una recompensa baja.
#   - Si ambos jugadores traicionan, ambos reciben una recompensa baja debido a la venganza.

payoff_matrix = {
    'cooperar': {'cooperar': (3, 3), 'traicionar': (0, 5)},
    'traicionar': {'cooperar': (5, 0), 'traicionar': (1, 1)}
}

print("Matriz de pago para el dilema del prisionero:")
for action1 in payoff_matrix:
    for action2 in payoff_matrix[action1]:
        payoff = payoff_matrix[action1][action2]
        print(f"{action1} vs {action2}: Jugador 1 recibe {payoff[0]}, Jugador 2 recibe {payoff[1]}")
