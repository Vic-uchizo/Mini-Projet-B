# =============================================================================
# Mini-Projet B - Integration numerique
# Fichier principal : definit le polynome et appelle toutes les methodes
# =============================================================================

from trapeze_python import integrale_trapeze_python
from trapeze_numpy import integrale_trapeze_numpy
from simpson import calculer_simpson_python, calculer_simpson_numpy
from moindre_rectangle import calculer_moindre_rectangle_python, calculer_moindre_rectangle_numpy
from graph import tracer_tous_les_graphiques
from performance import calculer_methode_analytique


# -----------------------------------------------------------------------------
# Coefficients du polynome f(x) = a + b*x + c*x^2 + d*x^3
# -----------------------------------------------------------------------------
a = 1
b = 2
c = 3
d = 4


def polynome(x):
    """Fonction a integrer : un polynome de 3e ordre."""
    return a + b * x + c * x**2 + d * x**3

polynome.coeff=[a,b,c,d] #pour faciulement recuperer les coefficient dans les fonctions

# -----------------------------------------------------------------------------
# Programme principal
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Bornes de l'intervalle (pas a/b : deja pris par les coefficients).
    x_min = 0
    x_max = 3

    # Nombre de segments.
    n = 10

    #Resultats reels de l'integrale
    print("Resultats analytiques : " ,calculer_methode_analytique(polynome, x_min, x_max))

    # On passe "polynome" en argument a chaque methode (sans parentheses).
    print("Rectangles (Python) :", calculer_moindre_rectangle_python(x_min, x_max, polynome, n))
    print("Rectangles (Numpy) :", calculer_moindre_rectangle_numpy(x_min,x_max,polynome,n))
    print("Trapezes   (Python) :", integrale_trapeze_python(x_min, x_max, polynome, n))
    print("Trapezes   (NumPy)  :", integrale_trapeze_numpy(x_min, x_max, polynome, n))
    print("Simpson    (Python) :", calculer_simpson_python(x_min, x_max, polynome, n))
    print("Simpson    (NumPy)  :", calculer_simpson_numpy(x_min, x_max, polynome, n))

    # Tracer les graphiques de comparaison (convergence, performance, erreur).
    tracer_tous_les_graphiques(polynome, x_min, x_max)
