import ast
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import statistics

from pso_algorithm import run_pso


def get_result_and_plot(g, m, data_config, w, c1, c2, X, target, config_code):
    results, score, scores_p, scores_g = run_pso(g, m, data_config, w, c1, c2, X)

    plt.figure(figsize=(6, 4))
    plt.axhline(
        y=target,
        marker="o",
        color="r",
        linestyle="--",
        label=f"Valor esperado ({target})",
    )
    plt.plot(scores_g)
    plt.title(
        f'Evolução dos Scores por Partícula (scores_p) - {data_config.get("problem")} - Configuração {config_code}'
    )
    plt.ylabel("Score")
    plt.grid(True)
    
    plt.savefig(f'images/config_0{config_code}_{data_config.get("problem")}.png')
    
    print(f'Melhor resultado configuração {config_code} - {data_config.get("problem")}: {statistics.median(scores_g)}')

    return {
        "results": results,
        "score": score,
        "scores_p": scores_p,
        "scores_g": scores_g,
        "median_score_p": statistics.median(scores_g),
    }


if __name__ == "__main__":
    g = 30
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
        },
    }
    all_results = []

    for problem, target in {"shubert": -186.7309, "camel": -1.0316}.items():
        data_config["problem"] = problem

        results_01 = get_result_and_plot(g, m, data_config, [0.9], 2, 2, None, target, 1)
        results_02 = get_result_and_plot(
            g, m, data_config, [0.9, 0.4], 2, 2, None, target, 2
        )
        results_03 = get_result_and_plot(
            g, m, data_config, None, 2.05, 2.05, 0.73, target, 3
        )

        for r in [results_01, results_02, results_03]:
            r["problem"] = problem
            all_results.append(r)

    # Criar um único DataFrame com todos os dados
    df = pd.DataFrame(all_results)
    df_grouped = df.groupby("problem")
    for problem, data in df_grouped:
        plt.figure(figsize=(6, 4))
        plt.boxplot(data["scores_g"], patch_artist=True)
        plt.title(f"Boxplot dos Scores por Partícula (scores_p) - {problem}")
        plt.ylabel("Score")
        plt.xlabel("Configurações")
        plt.grid(True)
        plt.savefig(f'images/boxplot_{problem}.png')

    # === Identificar os melhores resultados
    best_shubert = df[df["problem"] == "shubert"]
    best_shubert = best_shubert.loc[best_shubert["score"].idxmin()]

    best_camel = df[df["problem"] == "camel"]
    best_camel = best_camel.loc[best_camel["score"].idxmin()]

    # === Leitura dos dados do GA
    df_ga_shubert = pd.read_csv("melhores_fitness_shubert.csv", header=None)
    df_ga_camel = pd.read_csv("melhores_fitness_camel.csv", header=None)

    # === Gráfico de comparação SHUBERT
    plt.figure(figsize=(8, 5))
    plt.axhline(y=-186.7309, color="r", linestyle="--", label="Valor esperado (target)")
    plt.plot(best_shubert["scores_g"], 'o-', label="PSO", color="blue")
    plt.plot(ast.literal_eval(df_ga_shubert.iloc[7].values[1]), 'x-', label="GA", color="green")
    plt.title("Comparação da evolução do GA e PSO - Shubert")
    plt.xlabel("Iterações")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)
    plt.savefig('images/comparation_shubert.png')

    # === Gráfico de comparação CAMEL
    plt.figure(figsize=(8, 5))
    plt.axhline(y=-1.0316, color="r", linestyle="--", label="Valor esperado (target)")
    plt.plot(best_camel["scores_g"], 'o-', label="PSO", color="blue")
    plt.plot(ast.literal_eval(df_ga_camel.iloc[7].values[1]), 'x-', label="GA", color="green")
    plt.title("Comparação da evolução do GA e PSO - Camel")
    plt.xlabel("Iterações")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)
    plt.savefig('images/comparation_camel.png')

    plt.show()
