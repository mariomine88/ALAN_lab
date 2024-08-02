import numpy as np
from scipy.linalg import solve

# Funzione per calcolare la norma infinito di una matrice
def norma_infinito(A):
    return np.max(np.sum(np.abs(A), axis=1))

# Definizione delle matrici
matrici = {
    "A1": np.array([[3, 1, -1, 0], [0, 7, -3, 0], [0, -3, 9, -2], [0, 0, 4, -10]]),
    "A2": np.array([[2, 4, -2, 0], [1, 3, 0, 1], [3, -1, 1, 2], [0, -1, 2, 1]]),
}

# Creazione della matrice di Pascal
def matrice_pascal(n):
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            P[i, j] = np.math.factorial(i + j) / (np.math.factorial(i) * np.math.factorial(j))
    return P

matrici["P"] = matrice_pascal(10)

# Creazione della matrice tridiagonale
def matrice_tridiagonale(n):
    T = np.zeros((n, n))
    for i in range(n):
        T[i, i] = 2
        if i > 0:
            T[i, i-1] = -1
        if i < n-1:
            T[i, i+1] = -1
    return T

# Esempio con matricola 123456 (ultima cifra 6, penultima cifra 5)
d0 = 6
d1 = 5
n = 10 * (d1 + 1) + d0

matrici["T"] = matrice_tridiagonale(n)

# Calcolo della norma infinito per ogni matrice
for nome, A in matrici.items():
    print(f"Norma infinito della matrice {nome}: {norma_infinito(A)}")

# Calcolo del termine noto b e risoluzione del sistema Ax = b
for nome, A in matrici.items():
    n = A.shape[0]
    x_bar = np.ones(n)
    b = A.dot(x_bar)
    x = solve(A, b)
    print(f"Soluzione del sistema Ax = b per la matrice {nome}: {x}")

    # Calcolo di delta b e risoluzione del sistema perturbato
    delta_b = np.linalg.norm(b, np.inf) * np.array([(-0.01) ** (i % 2) for i in range(n)])
    b_perturbato = b + delta_b
    x_tilde = solve(A, b_perturbato)
    print(f"Soluzione del sistema Ax = (b + delta_b) per la matrice {nome}: {x_tilde}")

    # Confronto delle soluzioni
    differenza = np.linalg.norm(x - x_tilde, np.inf)
    print(f"Differenza tra le soluzioni per la matrice {nome}: {differenza}")
