import numpy as np
import matplotlib.pyplot as plt

# Dimensions de la cavité
longueur_x = 1.0
longueur_y = 1.0

# Vitesse de propagation
vitesse_onde = 1.0

# Nombre de modes superposés
nb_modes_x = 5
nb_modes_y = 5

# Grille 2D de calcul
nb_points_x = 150
nb_points_y = 150
x = np.linspace(0, longueur_x, nb_points_x)
y = np.linspace(0, longueur_y, nb_points_y)
X, Y = np.meshgrid(x, y)

# Amplitudes et phases aléatoires des modes
amplitudes = np.random.rand(nb_modes_x, nb_modes_y)
phases = 2 * np.pi * np.random.rand(nb_modes_x, nb_modes_y)

# Instants visualisés
liste_instants = [0, 0.5, 1.0, 1.5]

# Champ dans un système fermé (superposition de modes propres)
def champ_2D_ferme(X, Y, t):
    champ = np.zeros_like(X)
    for m in range(1, nb_modes_x + 1):
        for n in range(1, nb_modes_y + 1):
            kx = m * np.pi / longueur_x
            ky = n * np.pi / longueur_y
            omega = vitesse_onde * np.sqrt(kx**2 + ky**2)
            champ += amplitudes[m-1, n-1] * np.sin(kx * X) * np.sin(ky * Y) * np.cos(omega * t + phases[m-1, n-1])
    return champ

# Affichage
plt.figure(figsize=(10, 10))

for i, instant in enumerate(liste_instants, start=1):
    champ = champ_2D_ferme(X, Y, instant)
    plt.subplot(2, 2, i)
    plt.imshow(champ, extent=[0, longueur_x, 0, longueur_y], origin="lower", cmap="viridis")
    plt.title(f"t = {instant}")
    plt.colorbar()

plt.suptitle("Interférences 2D dans un système fermé")
plt.show()
