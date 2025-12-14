import matplotlib.pyplot as plt

type_lentille = input("Lentille C (convergente) ou D (divergente) : ").upper()
focale = float(input("Focale (cm) : "))
position_objet = float(input("Position de l'objet (cm) : "))

if type_lentille == "C":
    focale = abs(focale)
else:
    focale = -abs(focale)

position_lentille = 0
hauteur_objet = 2

distance_objet = abs(position_objet - position_lentille)
distance_image = 1e6 if distance_objet == abs(focale) else 1 / (1/focale - 1/distance_objet)

position_image = position_lentille + distance_image
hauteur_image = -hauteur_objet * distance_image / distance_objet

plt.figure(figsize=(9,4))
plt.axhline(0, color="black")

plt.axvline(position_lentille, color="blue")
plt.scatter([focale, -focale], [0,0], color='red')

plt.plot([position_objet, position_objet], [0, hauteur_objet], color="green")

plt.plot([position_objet, position_lentille], [hauteur_objet, hauteur_objet], color="orange")
if type_lentille == "C":
    plt.plot([position_lentille, position_image], [hauteur_objet, hauteur_image], color="orange")
else:
    plt.plot([position_lentille, position_lentille+5], [hauteur_objet, hauteur_image], linestyle="--", color="orange")
    plt.plot([position_lentille, position_image], [hauteur_objet, hauteur_image], color="orange")

plt.plot([position_objet, position_image], [hauteur_objet, hauteur_image], color="purple")

plt.plot([position_image, position_image], [0, hauteur_image], color="cyan")

plt.ylim(-5, 5)
plt.grid(True)
plt.show()
