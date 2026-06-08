from trapeze_python import integrale_trapeze_python
from trapeze_numpy import integrale_trapeze_numpy
from simpson import calculer_simpson_numpy,calculer_simpson_python
from moindre_rectangle import calculer_moindre_rectangle_numpy,calculer_moindre_rectangle_python
from timeit import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

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

def calculer_methode_analytique(f, inf, sup):
    """Valeur exacte de l'integrale du polynome a + b*x + c*x^2 + d*x^3."""
    a,b,c,d=f.coeff
    F_sup = a*sup + b*(sup**2)/2 + c*(sup**3)/3 + d*(sup**4)/4
    F_inf = a*inf + b*(inf**2)/2 + c*(inf**3)/3 + d*(inf**4)/4
    return F_sup - F_inf

def mesurer_temps(fonction, x_min, x_max, polynome, n):
    temps = timeit(lambda: fonction(x_min, x_max, polynome, n), number=100)    
    return temps

# -----------------------------------------------------------------------------
# Fonctions erreur entre les methodes et la valeur exacte
# -----------------------------------------------------------------------------

def erreur(fonction, polynome, x_min, x_max, n):
    """Ecart absolu entre la methode et la valeur exacte, pour n segments."""
    exacte = calculer_methode_analytique(polynome, x_min, x_max)
    approx = fonction(x_min, x_max, polynome, n)
    diff = abs(approx - exacte)
    # Si la diff est inférieure à la précision machine, on la bloque à 1e-15
    return max(diff, 1e-15)