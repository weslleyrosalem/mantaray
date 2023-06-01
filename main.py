import numpy as np
import matplotlib.pyplot as plt

# Bitstring objetivo
target_bitstring = np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])
# Função de fitness personalizada para a distância de Hamming
def fitness_custom(x):
    # Converte o vetor contínuo em uma bitstring
    bitstring = np.round(x).astype(int)
    # Calcula e retorna a distância de Hamming
    return np.sum(np.abs(bitstring - target_bitstring))

# Define o algoritmo Manta Ray Foraging Optimization.
def MRFO(n_iterations, n_manta_rays, dim, lower_bound, upper_bound, foraging_method, fitness=fitness_custom, tol=1e-5):
    # Inicializa a população de raias-mantas.
    manta_rays = np.random.uniform(lower_bound, upper_bound, (n_manta_rays, dim))

    # Avalia a aptidão inicial de cada raia-manta.
    fitness_values = np.apply_along_axis(fitness, 1, manta_rays)

    # Encontra a raia-manta com a melhor aptidão.
    best_fitness_index = np.argmin(fitness_values)
    best_fitness = fitness_values[best_fitness_index]
    best_manta_ray = np.copy(manta_rays[best_fitness_index])

    # Armazena a aptidão da melhor raia-manta para cada iteração
    best_fitness_history = []

    # Métodos de forrageamento
    foraging_methods = ['chain', 'cyclone', 'somersault']

    # Loop principal do algoritmo.
    for iteration in range(n_iterations):
        # Selecione o método de forrageamento para esta iteração
        selected_foraging_method = foraging_methods[
            iteration % len(foraging_methods)] if foraging_method == 'unified' else foraging_method

        for i in range(n_manta_rays):
            for d in range(dim):
                if selected_foraging_method == 'chain':
                    # Movimento de Cadeia (Chain)
                    manta_rays[i][d] += (np.mean(manta_rays[:, d]) - manta_rays[i][d]) * np.random.rand()
                elif selected_foraging_method == 'cyclone':
                    # Movimento de Ciclone (Cyclone)
                    manta_rays[i][d] += np.sin(np.random.uniform(-np.pi, np.pi)) * abs(
                        best_manta_ray[d] - manta_rays[i][d])
                elif selected_foraging_method == 'somersault':
                    # Movimento de Somersault
                    manta_rays[i][d] += np.random.uniform(-1, 1) * (upper_bound - lower_bound)

                # Garante que a posição da raia-manta está dentro dos limites.
                manta_rays[i][d] = np.clip(manta_rays[i][d], lower_bound, upper_bound)

            # Avalia a nova aptidão da raia-manta.
            new_fitness = fitness(manta_rays[i])

            # Se a nova aptidão é melhor, atualiza a aptidão e a melhor raia-manta se necessário.
            if new_fitness < fitness_values[i]:
                fitness_values[i] = new_fitness

                if new_fitness < best_fitness:
                    best_fitness = new_fitness
                    best_manta_ray = np.copy(manta_rays[i])

        # Registra a aptidão da melhor raia-manta para esta iteração
        best_fitness_history.append(best_fitness)

        # Verifica o critério de parada
        if best_fitness < tol:
            break

    # Garante que o histórico de aptidão seja sempre de tamanho n_iterations, preenchendo com o último valor de aptidão, se necessário
    while len(best_fitness_history) < n_iterations:
        best_fitness_history.append(best_fitness)

    return best_manta_ray, best_fitness, best_fitness_history

# Número de iterações
n_iterations = 100

# Número de execuções por método
n_runs = 10

# Chama o algoritmo MRFO para cada método de forrageamento e plota os resultados
methods = ['chain', 'cyclone', 'somersault', 'unified']
final_fitness_values = []

for method in methods:
    history_avg = np.zeros(n_iterations)

    for run in range(n_runs):
        _, _, history = MRFO(n_iterations=n_iterations, n_manta_rays=30, dim=12, lower_bound=0, upper_bound=1,
                             foraging_method=method)
        history_avg += np.array(history)

    history_avg /= n_runs
    final_fitness_values.append(history_avg[-1])
    plt.plot(history_avg, label=method)

# Informa qual método obteve o melhor resultado
best_method_index = np.argmin(final_fitness_values)
print(f"O método que obteve o melhor resultado foi: {methods[best_method_index]}")

plt.legend()
plt.xlabel('Iteration')
plt.ylabel('Average Best Fitness')
plt.show()
