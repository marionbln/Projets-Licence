import numpy as np
import matplotlib.pyplot as plt

# Paramètres physiques
vitesse_onde = 1.0
pas_espace = 0.01
pas_temps = 0.7 * pas_espace / vitesse_onde

# Taille du domaine
nb_x = 200
nb_y = 200
x = np.linspace(0, 1.0, nb_x)
y = np.linspace(0, 1.0, nb_y)
X, Y = np.meshgrid(x, y)

# Modes superposés
nb_modes_x = 5
nb_modes_y = 5

# Amplitudes et phases aléatoires
amplitudes = np.random.rand(nb_modes_x, nb_modes_y)
phases = 2 * np.pi * np.random.rand(nb_modes_x, nb_modes_y)

# Instants affichés
liste_instants = [0, 0.5, 1.0, 1.5]

# Champ 2D dans un système fermé (modes propres)
def champ_ferme(X, Y, t):
    champ = np.zeros_like(X)
    for m in range(1, nb_modes_x + 1):
        for n in range(1, nb_modes_y + 1):
            kx = m * np.pi
            ky = n * np.pi
            omega = vitesse_onde * np.sqrt(kx**2 + ky**2)
            champ += amplitudes[m-1, n-1] * np.sin(kx * X) * np.sin(ky * Y) * np.cos(omega * t + phases[m-1, n-1])
    return champ

# Affichage du champ pour plusieurs instants
plt.figure(figsize=(10, 10))

for i, instant in enumerate(liste_instants, start=1):
    champ = champ_ferme(X, Y, instant)
    plt.subplot(2, 2, i)
    plt.imshow(champ.T, origin="lower", cmap="viridis")
    plt.title(f"t = {instant}")
    plt.colorbar()

plt.suptitle("Interférences 2D dans un système fermé")
plt.show()
