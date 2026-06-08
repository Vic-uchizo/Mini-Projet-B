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


def erreur_python_numerique(inf, sup, f, n,):
    """Ecart entre la valeur numerique (rectangles) et la valeur exacte."""
    numerique = calculer_moindre_rectangle_python(inf, sup, f, n)
    exacte = calculer_methode_analytique(f, inf, sup)
    return abs(numerique - exacte)

def calculer_moindre_rectangle_numpy(inf,sup,f,n):
    # Créer les points x entre inf et sup
    largeur_segment = (sup - inf)/n
    valeur_x = np.linspace(inf, sup, n+1)
    valeur_y = f(valeur_x)
    hauteur_segment = (valeur_y[:-1] + valeur_y[1:]) / 2 # Calculer la hauteur moyenne de chaque rectangle
    # Calculer l'aire totale
    aire_totale = np.sum(hauteur_segment * largeur_segment)
    
    return aire_totale


# Test autonome (ne s'execute QUE si on lance ce fichier directement).
if __name__ == "__main__":
    a, b, c, d = 3, 2, 5, 1
    inf, sup, n = 40, 50, 10

    def polynome(x):
        return a + b*x + c*x**2 + d*x**3

    polynome.coeff=[a,b,c,d]

    print("Analytique :", calculer_methode_analytique(polynome, inf, sup))
    print("Numerique  :", calculer_moindre_rectangle_python(inf, sup, polynome, n))
    print("Erreur     :", erreur_python_numerique(inf, sup, polynome, n ))
    print("Methode moindre carre : ",calculer_moindre_rectangle_numpy(inf,sup,polynome,n))
