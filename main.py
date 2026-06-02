# =============================================================================
# Mini-Projet B - Integration numerique
# Fichier principal : definit le polynome et appelle les methodes d'integration
# =============================================================================

# On importe notre methode des trapezes (Python de base).
from trapeze_python import integrale_trapeze


# -----------------------------------------------------------------------------
# Coefficients du polynome f(x) = a + b*x + c*x^2 + d*x^3
# (a modifier selon les valeurs de l'enonce)
# -----------------------------------------------------------------------------
a = 1
b = 2
c = 3
d = 4


def polynome(x):
    """
    Notre fonction a integrer : un polynome de 3e ordre.
    Elle ne prend qu'un seul argument x ; les coefficients a, b, c, d
    sont pris dans les variables definies ci-dessus.
    """
    return a + b * x + c * x**2 + d * x**3


# -----------------------------------------------------------------------------
# Programme principal
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Bornes de l'intervalle d'integration.
    # /!\ On NE les appelle PAS a et b : ces noms servent deja aux coefficients
    #     du polynome ci-dessus. On utilise donc x_min et x_max pour eviter
    #     toute confusion.
    x_min = 0
    x_max = 3

    # Pas de resolution : nombre de segments.
    n = 10

    # On passe la fonction "polynome" en argument (sans les parentheses !).
    # integrale_trapeze va l'appeler elle-meme : polynome(x_gauche), etc.
    resultat = integrale_trapeze(x_min, x_max, polynome, n)

    print("Integrale approchee (trapezes, Python de base) :", resultat)
