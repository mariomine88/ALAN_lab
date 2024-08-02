import math

# Funzione per calcolare il polinomio di Taylor
def taylor_series_exp(x, N):
    return sum(x**n / math.factorial(n) for n in range(N + 1))

# Algoritmo 1
def algoritmo1(x_values, N_values):
    results = {}
    for x in x_values:
        results[x] = {}
        for N in N_values:
            approx = taylor_series_exp(x, N)
            exact = math.exp(x)
            rel_error = abs((exact - approx) / exact)
            abs_error = abs(exact - approx)
            results[x][N] = (approx, exact, rel_error, abs_error)
    return results

# Algoritmo 2
def algoritmo2(x_values, N_values):
    results = {}
    for x in x_values:
        results[x] = {}
        for N in N_values:
            approx_pos = taylor_series_exp(-x, N)
            approx_neg = 1 / approx_pos
            exact = math.exp(-x)
            rel_error = abs((exact - approx_neg) / exact)
            abs_error = abs(exact - approx_neg)
            results[x][N] = (approx_neg, exact, rel_error, abs_error)
    return results

# Parametri
x_values = [0.5, 30, -0.5, -30]
N_values = [3, 10, 50, 100, 150]

# Esecuzione degli algoritmi
results_alg1 = algoritmo1(x_values, N_values)
results_alg2 = algoritmo2(x_values, N_values)

# Stampa dei risultati
for x in x_values:
    print(f"Risultati per x = {x}:")
    for N in N_values:
        if x > 0:
            approx, exact, rel_error, abs_error = results_alg1[x][N]
        else:
            approx, exact, rel_error, abs_error = results_alg2[-x][N]
        print(f"  N = {N}: approx = {approx}, exact = {exact}, rel_error = {rel_error}, abs_error = {abs_error}")
