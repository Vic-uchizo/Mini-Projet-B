<<<<<<< HEAD
### Module : methode des RECTANGLES (Python de base) ###
# La fonction a integrer est passee en parametre (f), comme pour les trapezes.
=======
from main import *
import timeit
import numpy as np

### Module de programmation de la methode des moindres carres###
## Fonction de type p1 + p2*inf+p3*inf^2 +p4*inf^3 ###

inf=40
sup=50
n=100
>>>>>>> a3c651dcc14bf89f0bcb44068b166cba3633751b


def calculer_methode_analytique(a, b, c, d, inf, sup):
    """Valeur exacte de l'integrale du polynome a + b*x + c*x^2 + d*x^3."""
    F_sup = a*sup + b*(sup**2)/2 + c*(sup**3)/3 + d*(sup**4)/4
    F_inf = a*inf + b*(inf**2)/2 + c*(inf**3)/3 + d*(inf**4)/4
    return F_sup - F_inf


def calculer_moindre_rectangle_python(inf, sup, f, n):
    """Integrale de f sur [inf, sup] par la methode des rectangles."""
    largeur_segment = (sup - inf) / n
    Aire_rectangle_tot = 0
    i = inf
    while i < sup:
        hauteur_segment = (f(i) + f(i + largeur_segment)) / 2
        Aire_rectangle_tot += largeur_segment * hauteur_segment
        i = i + largeur_segment
    return Aire_rectangle_tot


def erreur_python_numerique(inf, sup, f, n, a, b, c, d):
    """Ecart entre la valeur numerique (rectangles) et la valeur exacte."""
    numerique = calculer_moindre_rectangle_python(inf, sup, f, n)
    exacte = calculer_methode_analytique(a, b, c, d, inf, sup)
    return abs(numerique - exacte)


# Test autonome (ne s'execute QUE si on lance ce fichier directement).
if __name__ == "__main__":
    a, b, c, d = 12, 13, 14, 15
    inf, sup, n = 40, 50, 100

<<<<<<< HEAD
    def polynome(x):
        return a + b*x + c*x**2 + d*x**3

    print("Analytique :", calculer_methode_analytique(a, b, c, d, inf, sup))
    print("Numerique  :", calculer_moindre_rectangle_python(inf, sup, polynome, n))
    print("Erreur     :", erreur_python_numerique(inf, sup, polynome, n, a, b, c, d))
=======
print("Methode analytique : ",calculer_methode_analytique(a,b,c,d,inf,sup))
print("Methode numerique : ",calculer_moindre_rectangle_python(inf,sup,n))
print("Erreur ", erreur_python_numerique(inf,sup,n,a,b,c,d))

# Mesure du temps avec timeit
temps = timeit.timeit('calculer_moindre_rectangle_python(inf,sup,n)',globals=globals(), number=100)
print(f"Temps moyen par execution : {temps/1000*100:.6f} ms")

### Methode numpy ###

def calculer_moindre_rectangle_numpy(a,b,c,d,inf,sup,n):
    # Créer les points x entre inf et sup
    largeur_segment = (sup - inf)/n
    valeur_x = np.linspace(inf, sup, n+1)
    valeur_y = np.polyval([d, c, b, a], valeur_x) 
    hauteur_segment = (valeur_y[:-1] + valeur_y[1:]) / 2 # Calculer la hauteur moyenne de chaque rectangle
    # Calculer l'aire totale
    aire_totale = np.sum(hauteur_segment * largeur_segment)
    
    return aire_totale

print("Methode numerique numpy : ",calculer_moindre_rectangle_numpy(a,b,c,d,inf,sup,n))

temps = timeit.timeit('calculer_moindre_rectangle_numpy(a,b,c,d,inf,sup,n)',globals=globals(), number=100)
print(f"Temps moyen par execution pour numpy: {temps/1000*100:.6f} ms")
>>>>>>> a3c651dcc14bf89f0bcb44068b166cba3633751b
