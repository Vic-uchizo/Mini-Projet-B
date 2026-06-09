### Module : methode des RECTANGLES (Python de base) ###
# La fonction a integrer est passee en parametre (f), comme pour les trapezes.
import numpy as np



def calculer_moindre_rectangle_python(inf, sup, f, n):
    """Integrale de f sur [inf, sup] par la methode des rectangles."""
    largeur_segment = (sup - inf) / n
    Aire_rectangle_tot = 0
    for i in range(n):
        borne=inf+i*largeur_segment
        hauteur_segment = (f(borne + largeur_segment/ 2)) 
        Aire_rectangle_tot += largeur_segment * hauteur_segment
    return Aire_rectangle_tot


def calculer_moindre_rectangle_numpy(inf,sup,f,n):
    # Créer les points x entre inf et sup
    largeur_segment = (sup - inf)/n
    valeur_x = np.linspace(inf+largeur_segment/2, sup-largeur_segment/2, n)
    valeur_y = f(valeur_x)
    # Calculer l'aire totale
    aire_totale = np.sum(valeur_y * largeur_segment)
    
    return aire_totale