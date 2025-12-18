# Simulation d’ondes 2D : systèmes fermé et ouvert

Ce projet illustre la propagation d’ondes dans un domaine 2D en utilisant une méthode numérique simple (FDTD).

## Système fermé
Les bords sont réfléchissants : l’onde rebondit et reste piégée dans le domaine.  
Ce type de système permet d’observer des interférences durables et des modes propres.

## Système ouvert
Les bords sont absorbants : l’onde disparaît progressivement en atteignant les limites.  
Le domaine se comporte comme un espace infini où l’énergie peut sortir.

## Modèle physique
Équation d’onde 2D :
\[
\frac{\partial^2 u}{\partial t^2}
= c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)
\]

Schéma numérique explicite :
\[
u^{t+\Delta t} = 2u^t - u^{t-\Delta t} + c^2 \Delta t^2 \nabla^2 u^t
\]

Une source ponctuelle au centre génère l’onde.



