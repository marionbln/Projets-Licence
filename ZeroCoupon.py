import numpy as np
import matplotlib.pyplot as plt

# Taux spot annuels en %
maturities = np.array([1, 2, 3, 5, 10])
spot_rates = np.array([2.0, 2.2, 2.5, 3.0, 3.5]) / 100

# Calcul DF = 1 / (1+r)^t
DF = 1 / (1 + spot_rates)**maturities

# Taux zero-coupon = spot (ici donné directement)
ZC = spot_rates

# Taux forward entre t1 et t2
def forward_rate(t1, t2):
    return ( (DF[t1] / DF[t2]) ** (1/(t2 - t1)) - 1 )

# Exemple forward entre 1 an et 2 ans
f_1_2 = forward_rate(0, 1)
print("Forward 1→2 ans :", round(f_1_2*100, 4), "%")

# Tracé
plt.plot(maturities, spot_rates*100, label="Spot")
plt.plot(maturities, ZC*100, label="Zero-coupon")
plt.plot(maturities, -np.log(DF)/maturities*100, label="Instantané approx.")
plt.xlabel("Maturité (années)")
plt.ylabel("Taux (%)")
plt.legend()
plt.grid()
plt.show()
