import numpy as np



# Méthode python

def calculer_f(polynome, x):
    f = polynome[0] + polynome[1]*x + polynome[2]*x*x + polynome[3]*x*x*x
    return f

def calculer_simpson(a, b, polynome, n):
    aire = 0
    position = a
    intervalle = (b - a) / n
    
    for _ in range(n):
        aire += (intervalle / 6) * (calculer_f(polynome, position) + 4 * calculer_f(polynome, (position + intervalle / 2)) + calculer_f(polynome, (position + intervalle)))
        position += intervalle

    return aire


# Méthode numpy

