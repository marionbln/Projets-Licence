import numpy as np

def binomial_call_CRR(S0, K, T, r, sigma, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r*dt) - d) / (u - d)

    # Prix de l'actif à maturité
    S_T = np.array([S0 * u**j * d**(n-j) for j in range(n+1)])

    # Valeur du call à maturité
    C_T = np.maximum(S_T - K, 0)

    # Backward induction
    for i in range(n-1, -1, -1):
        C_T = np.exp(-r*dt) * (p * C_T[1:i+2] + (1-p) * C_T[0:i+1])

    return C_T[0]

# Exemple
price = binomial_call_CRR(S0=100, K=100, T=1, r=0.025, sigma=0.20, n=100)
print("Prix du call (CRR) :", price)
