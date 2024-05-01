import numpy as np
import gym

# Crear el entorno del Taxi
env = gym.make("Taxi-v3")

# Inicializar la tabla Q con ceros
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Definir hiperparámetros
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Probabilidad de exploración

# Ejecutar episodios de entrenamiento
num_episodes = 1000
for _ in range(num_episodes):
    state = env.reset()
    done = False
    while not done:
        # Elegir una acción utilizando la política ε-greedy
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Exploración aleatoria
        else:
            action = np.argmax(Q[state])  # Explotación basada en la tabla Q
        
        # Realizar la acción y obtener la recompensa y el próximo estado
        next_state, reward, done, _ = env.step(action)
        
        # Actualizar la tabla Q utilizando la ecuación de Q-Learning
        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        
        # Actualizar el estado actual al próximo estado
        state = next_state

# Imprimir la tabla Q después del entrenamiento
print("Tabla Q después del entrenamiento:")
print(Q)
