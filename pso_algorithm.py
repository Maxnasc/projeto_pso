import random
import math
import statistics

def shubert(x1, x2):
    sum1 = sum(i * math.cos((i + 1) * x1 + i) for i in range(1, 6))
    sum2 = sum(i * math.cos((i + 1) * x2 + i) for i in range(1, 6))
    return sum1 * sum2
            
def camel(x1, x2):
    term1 = (4 - 2.1 * x1**2 + x1**4 / 3) * x1**2
    term2 = x1 * x2
    term3 = (-4 + 4 * x2**2) * x2**2
    return term1 + term2 + term3

def get_r():
    return random.random()

def initialize(m, data_config):
    x = [[random.uniform(data_config.get('range').get('x1').get('base'), data_config.get('range').get('x1').get('top')),
         random.uniform(data_config.get('range').get('x2').get('base'), data_config.get('range').get('x2').get('top'))] for i in range(m)]

    v = [[random.uniform(data_config.get('v_max').get('x1').get('min'), data_config.get('v_max').get('x1').get('max')),
         random.uniform(data_config.get('v_max').get('x2').get('min'), data_config.get('v_max').get('x2').get('max'))] for i in range(m)]
    
    return x, v

def run_function(data_config, variables):
    if data_config.get('problem') == 'shubert':
        return [shubert(x[0], x[1]) for x in variables]
    else:
        return [camel(x[0], x[1]) for x in variables]

def get_best_result(scores):
    best_idx = max(scores.items(), key=lambda item: item[1])[0]
    best_value = (1 / scores[best_idx]) - 200  # Corrigir a volta da translação
    return best_value

def get_mean_fitness(scores):
    mean_fitness = statistics.mean(scores.values())
    mean_fitness_tranformed = (1 / mean_fitness) - 200  # Corrigir a volta da translação
    return mean_fitness_tranformed

def get_metrics(best_results):
    return {
        'mean': statistics.mean(best_results),
        'median': statistics.median(best_results),
        'max': max(best_results),
        'min': min(best_results)
    }

def run_pso(generations, m, data_config, w, c1, c2, X):
    x, v = initialize(m, data_config)
    p = x
    g = x[0]
    best_results = []
    global_result = []
    
    # Primeira avaliação
    scores_x = run_function(data_config, x)
    scores_p = scores_x
    score_g = scores_x[0]
    
    for gen in range(generations):
        # Ajustando o valor de w, se necessário
        if not X:
            w_now = max(w) - gen*((max(w)-min(w))/generations)
    
        best_results.append(scores_p)
        # Coleta a fitness média
        global_result.append(score_g)
        
        for i in range(m):
            scores_x = run_function(data_config, x)
            if scores_x[i] < scores_p[i]:
                p[i] = x[i]
                scores_p[i] = scores_x[i]
                if scores_x[i] < score_g:
                    g = x[i]
                    score_g = scores_x[i]
            for j in range(len(x[i])):
                r1, r2 = get_r(), get_r()
                if not X:
                    v[i][j] = w_now*v[i][j] + c1*r1*(p[i][j] - x[i][j]) + c2*r2*(g[j] - x[i][j])
                else:
                    v[i][j] = X*(v[i][j] + c1*r1*(p[i][j] - x[i][j]) + c2*r2*(g[j] - x[i][j]))
                if v[i][j] < data_config['v_max'][f'x{j+1}']['min']:
                    v[i][j] = data_config['v_max'][f'x{j+1}']['min']
                if v[i][j] > data_config['v_max'][f'x{j+1}']['max']:
                    v[i][j] = data_config['v_max'][f'x{j+1}']['max']
            x[i] = [x[i][k] + v[i][k] for k in range(len(x[i]))]
            if x[i][j] < data_config['range'][f'x{j+1}']['base']:
                x[i][j] = data_config['range'][f'x{j+1}']['base']
            if x[i][j] > data_config['range'][f'x{j+1}']['top']:
                x[i][j] = data_config['range'][f'x{j+1}']['top']
    return g, score_g, best_results, global_result

if __name__=="__main__":
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
    w = 0.9
    c1 = 2
    c2 = 2
    result, score = run_pso(g, m, data_config, w, c1, c2)
    print(score)