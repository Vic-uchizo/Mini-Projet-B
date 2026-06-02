# =============================================================================
# Methode des TRAPEZES, version VECTORISEE avec NumPy
# =============================================================================
# Meme principe que la version Python de base, mais SANS boucle for :
# NumPy calcule sur tout le tableau d'un coup, ce qui est beaucoup plus rapide.
# =============================================================================

import numpy as np

def integrale_trapeze_numpy(a, b, f, n):

    # Largeur d'un segment.
    h = (b - a) / n

    # Tous les points x d'un coup : x_0, x_1, ..., x_n  (n+1 points).
    x = np.linspace(a, b, n + 1)

    # Hauteur de la courbe en chaque point (f appliquee a tout le tableau).
    y = f(x)

    # Pour chaque trapeze, on a besoin de son bord gauche et de son bord droit :
    y_gauche = y[:-1]   # tous les points SAUF le dernier  -> bords gauches
    y_droite = y[1:]    # tous les points SAUF le premier  -> bords droits

    # Aire de chaque trapeze (meme formule que la version Python).
    aires = h * (y_gauche + y_droite) / 2

    # On additionne l'aire de tous les trapezes.
    return np.sum(aires)
