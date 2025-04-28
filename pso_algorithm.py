import random
import math

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

    v = [[random.random(), random.random()] for i in range(m)]
    
    return x, v

def run_function(data_config, variables):
    if data_config.get('problem') == 'shubert':
        return [shubert(x[0], x[1]) for x in variables]
    else:
        return [camel(x[0], x[1]) for x in variables]

def run_pso(generations, m, data_config, w, c1, c2):
    x, v = initialize(m, data_config)
    p = x
    g = x[0]
    
    # Primeira avaliação
    scores_x = run_function(data_config, x)
    scores_p = scores_x
    score_g = scores_x[0]
    
    for gen in range(generations):
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
                v[i][j] = w*v[i][j] + c1*r1*(p[i][j] - x[i][j]) + c2*r2*(g[j] - x[i][j])
            x[i] = [x[i][k] + v[i][k] for k in range(len(x[i]))]
    return g

if __name__=="__main__":
    g = 100
    m = 100
    data_config = {
        "problem": "shubert",
        "range": {
            "x1": {"base": -10, "top": 10},
            "x2": {"base": -10, "top": 10},
        },
    }
    w = 0.9
    c1 = 2
    c2 = 2
    result = run_pso(g, m, data_config, w, c1, c2)
    a=1