# Aritmetica di macchina
d0 = 6
d1 = 5
a_values = [(d0 + 1) * 10**i for i in range(7)]
b = (d1 + 1) * 10**20
c = -b

# Calcoli
results = []
for a in a_values:
    result1 = (a + b) + c
    result2 = a + (b + c)
    results.append((a, result1, result2))

# Stampa i risultati
for i, (a, res1, res2) in enumerate(results):
    print(f"Per a = {a}: (a + b) + c = {res1}, a + (b + c) = {res2}")
