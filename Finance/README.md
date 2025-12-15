# Présentation des modèles binomiaux pour la valorisation d’options

Ce document présente les principaux modèles binomiaux abordés dans le cours "Principes de Valorisation" d’Olivier Drean :  
- le modèle de Cox–Ross–Rubinstein (CRR),  
- le modèle de Jarrow–Rudd (JR),  
- le modèle de Tian,  
- le modèle de Trigeorgis.

Ces modèles reposent tous sur le cadre binomial standard, mais diffèrent dans la manière dont ils définissent les paramètres de l’arbre : la hausse (u), la baisse (d) et la probabilité neutre au risque (p).

Ils visent à approximer le comportement du sous-jacent sous mesure risque-neutre et à converger, lorsque le nombre de pas n augmente, vers le prix donné par le modèle de Black–Scholes.

---

## 1. Modèle de Cox–Ross–Rubinstein (CRR)

### Hypothèses et idées principales
Le modèle CRR est le modèle binomial le plus classique. Il repose sur les hypothèses standard :

- Le sous-jacent suit un processus log-normal.  
- Les rendements sont indépendants et identiquement distribués.  
- Les marchés sont parfaits (pas de coûts de transaction, possibilité de couverture continue).  
- La volatilité est constante.  

CRR impose une construction symétrique de l’arbre à chaque pas de temps pour reproduire la volatilité du sous-jacent.

### Paramétrisation
Pour un pas de temps Δt :
- \( u = e^{\sigma \sqrt{\Delta t}} \)
- \( d = 1/u \)
- \( p = \frac{e^{r \Delta t} - d}{u - d} \)

### Avantages
- Simple, robuste, largement utilisé.  
- Convergence rapide vers Black–Scholes.  
- Arbre recombina nt (structure stable et efficace).

### Limites
- Suppose une volatilité constante.  
- Ne permet pas d’adapter finement la dissymétrie des rendements.  
- Les distributions de prix sont nécessairement symétriques.

---

## 2. Modèle de Jarrow–Rudd (JR)

### Hypothèses et idées principales
Le modèle JR modifie le CRR pour imposer que la probabilité neutre au risque soit égale à 0.5.  
Ce choix simplifie l’arbre et permet de contrôler la dissymétrie à travers u et d.

### Paramétrisation
- Probabilité : \( p = 0.5 \)  
- Paramètres :
  - \( u = e^{(r - \frac{\sigma^2}{2})\Delta t + \sigma \sqrt{\Delta t}} \)
  - \( d = e^{(r - \frac{\sigma^2}{2})\Delta t - \sigma \sqrt{\Delta t}} \)

### Avantages
- Construction simple de l’arbre.  
- Peut représenter une distribution asymétrique.  
- Reproduit la dérive correcte du processus sous-jacent.

### Limites
- Convergence parfois plus lente que CRR.  
- Sensible aux valeurs paramétriques (u et d peuvent devenir trop extrêmes).  
- La contrainte p = 0.5 n’est pas nécessairement naturelle.

---

## 3. Modèle de Tian

### Hypothèses et objectifs
Le modèle Tian a été conçu pour améliorer l’adéquation entre l’arbre binomial et les moments du processus continu.

Contrairement au CRR qui reproduit essentiellement la volatilité, Tian ajuste :
- le premier moment,
- le second moment (variance),
- le troisième moment (skewness).

### Paramétrisation
Tian définit u, d et p via un système d’équations afin que les trois premiers moments du mouvement brownien géométrique soient respectés.

### Avantages
- Reproduction plus fidèle de la distribution théorique.  
- Peut fournir une meilleure approximation sur des maturités longues.

### Limites
- Le cours indique que « la convergence n’est pas certaine ».  
- Paramètres parfois instables.  
- Arbre susceptible de produire des valeurs extrêmes pour u et d.  
- Peut donner des résultats moins fiables pour de grands n.

---

## 4. Modèle de Trigeorgis

### Hypothèses et idées principales
Le modèle Trigeorgis vise à corriger certains défauts de CRR et JR en proposant une paramétrisation plus lisse, fondée sur un ajustement conjoint de la dérive et de la volatilité.

Il repose notamment sur une approximation différente de la variance cumulée.

### Paramétrisation
La définition de u, d et p dans ce modèle repose sur :

- une volatilité "modifiée",
- une dérive adaptée,
- une symétrie relative corrigée.

### Avantages
- Bonne stabilité numérique.  
- Convergence généralement correcte.  
- Moins sensible aux paramètres que JR ou Tian.

### Limites
- Convergence parfois moins rapide que CRR.  
- Moins théoriquement fondé que CRR.  
- Nécessite un ajustement numérique supplémentaire.

---

## 5. Comparaison synthétique

| Modèle | Robustesse | Convergence | Paramétrisation | Points faibles |
|--------|------------|-------------|------------------|----------------|
| CRR | Très bonne | Rapide | Simple et symétrique | Volatilité constante, distribution limitée |
| JR | Moyenne | Correcte | Probabilité 0.5 | Paramètres parfois extrêmes |
| Tian | Variable | Non garantie | Reproduit plusieurs moments | Instabilité, résultats irréguliers |
| Trigeorgis | Bonne | Correcte | Ajustements modérés | Moins rigoureux que CRR |

---

## Conclusion

Les quatre modèles appartiennent tous à la même famille des modèles binomiaux, mais leur comportement diffère sensiblement en pratique.

- CRR est le plus stable et reste la référence.  
- JR et Trigeorgis offrent des alternatives correctes dans certaines situations.  
- Tian, bien que théoriquement sophistiqué, peut être instable et ne garantit pas la convergence.

Ce panorama permet de comprendre les enjeux liés au choix d’un modèle binomial avant implémentation, en particulier pour des questions de stabilité et de précision.

