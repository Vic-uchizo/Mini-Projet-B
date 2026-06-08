import numpy as np

# Méthode python

def calculer_simpson_python(a, b, polynome, n):
    """
    Approximation de l'intégrale d'un polynôme via la méthode composite de Simpson.
    Utilise une simple boucle 'for' (Python natif).
    
    Arguments :
    a, b     -- Bornes de l'intervalle d'intégration.
    polynome -- Liste des 4 coefficients du polynôme.
    n        -- Nombre de sous-intervalles.
    """
    aire = 0
    position = a
    intervalle = (b - a) / n
    
    for _ in range(n):
        # Application de la formule de Simpson sur le sous-intervalle actuel
        aire += (intervalle / 6) * (polynome(position) + 
                                    4 * polynome(position + intervalle / 2) + 
                                    polynome(position + intervalle))
        position += intervalle

    return aire


# Méthode numpy

def calculer_simpson_numpy(a, b, polynome, n):
    """
    Approximation de l'intégrale par la méthode de Simpson, optimisée avec NumPy.
    Élimine les boucles au profit de calculs vectorisés pour des performances maximales.
    """
    # Génération de la grille : on demande 2n + 1 points pour inclure 
    # à la fois les bords des intervalles et leurs milieux.
    position = np.linspace(a, b, 2*n + 1)

    # Évaluation du polynôme sur toute la grille en une seule opération (broadcasting)
    f = polynome(position)

    # Application des poids de Simpson via le découpage du tableau (slicing) :
    # f[0] et f[-1] : extrémités (poids 1)
    # f[1::2]       : tous les indices impairs = les milieux (poids 4)
    # f[2:-1:2]     : tous les indices pairs internes = les frontières (poids 2)
    aire = ((b-a)/n)/6 * (f[0] + f[-1] + 4 * np.sum(f[1::2]) + 2 * np.sum(f[2:-1:2]))
    return aire