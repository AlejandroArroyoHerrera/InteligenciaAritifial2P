# Función Minimax con poda alfa-beta para el juego de Nim
def nim_alpha_beta(board, alpha, beta, maximizing_player):
    if sum(board) == 0:
        return -1
    if max(board) == 0:
        return 1
    if maximizing_player:
        max_eval = -math.inf
        for i in range(len(board)):
            if board[i] > 0:
                for j in range(1, board[i] + 1):
                    new_board = board[:]
                    new_board[i] -= j
                    eval = nim_alpha_beta(new_board, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(len(board)):
            if board[i] > 0:
                for j in range(1, board[i] + 1):
                    new_board = board[:]
                    new_board[i] -= j
                    eval = nim_alpha_beta(new_board, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Simulamos el juego de Nim utilizando Minimax con poda alfa-beta
board = [3, 4, 5]
alpha = -math.inf
beta = math.inf
winner = nim_alpha_beta(board, alpha, beta, True)
if winner == 1:
    print("Ganador: Jugador 1")
else:
    print("Ganador: Jugador 2")
