import numpy as np
import matplotlib.pyplot as plt

# Paramètres du polymère
nb_monomeres = 50
longueur_liaison = 1.0
amplitude_bruit = 0.3
nb_iterations = 500

# Initialisation de la chaîne (ligne droite)
positions = np.zeros((nb_monomeres, 2))
for i in range(1, nb_monomeres):
    positions[i] = positions[i-1] + np.array([longueur_liaison, 0])

# Mouvement brownien + correction de longueur
def mise_a_jour(positions):
    # Ajout bruit brownien à tous les monomères sauf le premier (point d'ancrage)
    bruit = amplitude_bruit * np.random.randn(nb_monomeres, 2)
    positions += bruit

    # Correction des distances pour garder des segments de longueur fixe
    for i in range(1, nb_monomeres):
        vecteur = positions[i] - positions[i-1]
        distance = np.linalg.norm(vecteur)
        if distance != 0:
            positions[i] = positions[i-1] + (vecteur / distance) * longueur_liaison

    return positions

# Simulation et affichage
plt.ion()
fig, ax = plt.subplots(figsize=(6,6))

for step in range(nb_iterations):
    positions = mise_a_jour(positions)

    ax.clear()
    ax.plot(positions[:,0], positions[:,1], '-o', markersize=3)
    ax.set_title(f"Polymère 2D – étape {step}")
    ax.set_aspect("equal")
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    plt.pause(0.01)

plt.ioff()
plt.show()
