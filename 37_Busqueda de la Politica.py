import numpy as np

# Definir funciones para la evaluación de la política y la mejora de la política
def policy_evaluation(policy, env, theta=0.0001, discount_factor=1.0):
    V = np.zeros(env.nS)
    while True:
        delta = 0
        for s in range(env.nS):
            v = 0
            for a, action_prob in enumerate(policy[s]):
                for prob, next_state, reward, done in env.P[s][a]:
                    v += action_prob * prob * (reward + discount_factor * V[next_state])
            delta = max(delta, np.abs(v - V[s]))
            V[s] = v
        if delta < theta:
            break
    return np.array(V)

def policy_improvement(env, policy_eval_fn=policy_evaluation, discount_factor=1.0):
    policy = np.ones([env.nS, env.nA]) / env.nA
    while True:
        current_policy = policy.copy()
        V = policy_eval_fn(policy, env, discount_factor)
        for s in range(env.nS):
            q_values = np.zeros(env.nA)
            for a in range(env.nA):
                for prob, next_state, reward, done in env.P[s][a]:
                    q_values[a] += prob * (reward + discount_factor * V[next_state])
            best_action = np.argmax(q_values)
            policy[s] = np.eye(env.nA)[best_action]
        if np.array_equal(current_policy, policy):
            break
    return policy

# Ejemplo de uso:
env = gym.make('FrozenLake-v0')
optimal_policy = policy_improvement(env)
print("Politica optima:")
print(optimal_policy)
