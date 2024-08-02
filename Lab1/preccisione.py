import numpy as np

# Precisione in singola precisione
def machine_epsilon_single():
    eps = 1.0
    while (1.0 + eps/2) != 1.0:
        eps /= 2
    return eps

# Precisione in doppia precisione
def machine_epsilon_double():
    eps = np.float64(1.0)
    while (np.float64(1.0) + eps/2) != np.float64(1.0):
        eps /= 2
    return eps

eps_single = machine_epsilon_single()
eps_double = machine_epsilon_double()

print(f"Precisione di macchina in singola precisione: {eps_single}")
print(f"Precisione di macchina in doppia precisione: {eps_double}")
