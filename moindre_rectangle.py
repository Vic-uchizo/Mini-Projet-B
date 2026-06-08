### Module : methode des RECTANGLES (Python de base) ###
# La fonction a integrer est passee en parametre (f), comme pour les trapezes.
import numpy as np



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


def calculer_moindre_rectangle_numpy(inf,sup,f,n):
    # Créer les points x entre inf et sup
    largeur_segment = (sup - inf)/n
    valeur_x = np.linspace(inf, sup, n+1)
    valeur_y = f(valeur_x)
    hauteur_segment = (valeur_y[:-1] + valeur_y[1:]) / 2 # Calculer la hauteur moyenne de chaque rectangle
    # Calculer l'aire totale
    aire_totale = np.sum(hauteur_segment * largeur_segment)
    
    return aire_totale