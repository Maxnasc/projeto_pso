import pandas as pd
import matplotlib.pyplot as plt
import itertools

from pso_algorithm import run_pso

def get_result_and_plot(g, m, data_config, w, c1, c2, X):
    return run_pso(g, m, data_config, w, c1, c2, X)

if __name__ == "__main__":
    g = 100
    m = 100
    data_config = {
        "problem": "shubert",
        "range": {
            "x1": {"base": -10, "top": 10},
            "x2": {"base": -10, "top": 10},
        },
        "v_max": {
            "x1": {"min": -1, "max": 1},
            "x2": {"min": -1, "max": 1},
        }
    }
    
    # Combinação 01 - Shubert
    problem = "shubert"
    w = [0.9]
    c1 = 2
    c2 = 2
    
    result_1, score_1 = get_result_and_plot(g, m, data_config, w, c1, c2, None)
    print(result_1, score_1)
    
    # Combinação 01 - Shubert
    problem = "shubert"
    w = [0.9, 0.4]
    c1 = 2
    c2 = 2
    
    result_2, score_2 = get_result_and_plot(g, m, data_config, w, c1, c2, None)
    print(result_2, score_2)
    
    # Combinação 01 - Shubert
    problem = "shubert"
    X = 0.73
    c1 = 2.05
    c2 = 2.05
    
    result_3, score_3 = get_result_and_plot(g, m, data_config, None, c1, c2, X)
    print(result_3, score_3)
    
    
    
    # # Criar DataFrame
    # df = pd.DataFrame(results)

    # # Separar Shubert e Camel
    # df_shubert = df[df["problem"] == "shubert"]
    # df_camel = df[df["problem"] == "camel"]

    # # Plotar boxplot para Shubert
    # fig, ax = plt.subplots(figsize=(20, 10))

    # # Ordenar do pior para o melhor (maior mínimo -> menor mínimo)
    # df_shubert_sorted = df_shubert.sort_values(by="min", ascending=False)

    # labels = []
    # data = []

    # for idx, row in df_shubert_sorted.iterrows():
    #     label = f"{row['selection_method']}|mut={row['mutation_prob']}|cross={row['crossover_prob']}"
    #     labels.append(label)
    #     data.append(row["fitness_values"])

    # ax.boxplot(data, showfliers=False)
    # ax.set_xticklabels(labels, rotation=90)
    # ax.set_title("Shubert - Comparação de Configurações (Ordenado)")
    # ax.set_ylabel("Fitness Final")
    # plt.tight_layout()

    # # Plotar boxplot para Camel
    # fig, ax = plt.subplots(figsize=(20, 10))

    # # Ordenar também para Camel
    # df_camel_sorted = df_camel.sort_values(by="min", ascending=False)

    # labels = []
    # data = []

    # for idx, row in df_camel_sorted.iterrows():
    #     label = f"{row['selection_method']}|mut={row['mutation_prob']}|cross={row['crossover_prob']}"
    #     labels.append(label)
    #     data.append(row["fitness_values"])

    # ax.boxplot(data, showfliers=False)
    # ax.set_xticklabels(labels, rotation=90)
    # ax.set_title("Camel - Comparação de Configurações (Ordenado)")
    # ax.set_ylabel("Fitness Final")
    # plt.tight_layout()

    # # Plot da evolução com os melhores parâmetros
    # # Shubert
    # best_shubert = df_shubert.loc[df_shubert["min"].idxmin()]
    # best_shubert_print = best_shubert.drop(columns="fitness_values")
    # print(f"Melhor configuração Shubert: {best_shubert_print}")
    # valores_fitness = best_shubert["fitness_values"]
    # # Plotar
    # plt.figure(figsize=(10, 6))
    # plt.plot(
    #     range(1, len(valores_fitness) + 1),
    #     valores_fitness,
    #     marker="o",
    #     label="Fitness por execução",
    # )
    # plt.axhline(
    #     y=-186.7309, color="r", linestyle="--", label="Valor esperado (-183.7309)"
    # )

    # plt.title("Evolução do Fitness - Melhor Configuração Shubert")
    # plt.xlabel("Geração")
    # plt.ylabel("Fitness")
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()

    # # camel
    # best_camel = df_camel.loc[df_camel["min"].idxmin()]
    # best_camel_print = best_camel.drop(columns="fitness_values")
    # print(f"Melhor configuração Camel: {best_camel_print}")
    # valores_fitness = best_camel["fitness_values"]
    # # Plotar
    # plt.figure(figsize=(10, 6))
    # plt.plot(
    #     range(1, len(valores_fitness) + 1),
    #     valores_fitness,
    #     marker="o",
    #     label="Fitness por execução",
    # )
    # plt.axhline(
    #     y=-1.0316, color="r", linestyle="--", label="Valor esperado (-183.7309)"
    # )

    # plt.title("Evolução do Fitness - Melhor Configuração camel")
    # plt.xlabel("Geração")
    # plt.ylabel("Fitness")
    # plt.legend()
    # plt.grid(True)
    # plt.tight_layout()

    # # Mostrar gráficos
    # plt.show()
