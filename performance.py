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

'''
polynome.coeff=[a,b,c,d] #pour faciulement recuperer les coefficient dans les fonctions

# Variables pour la boucle timeit
x_min = 0
x_max = 3
n = 10


temps_moindre_rectangle_python = timeit('calculer_moindre_rectangle_python(x_min, x_max, polynome, n)', globals=globals(), number=100)
print(f"Rectangles (Python) : {1000*temps_moindre_rectangle_python/(100):.6f} ms")

temps_moindre_rectangle_numpy = timeit('calculer_moindre_rectangle_numpy(x_min, x_max, polynome, n)', globals=globals(), number=100)
print(f"Rectangles (NumPy)  : {1000*temps_moindre_rectangle_numpy/(100):.6f} ms")

temps_trapeze_python = timeit('integrale_trapeze_python(x_min, x_max, polynome, n)', globals=globals(), number=100)
print(f"Trapezes   (Python) : {1000*temps_trapeze_python/(100):.6f} ms")

temps_trapeze_numpy = timeit('integrale_trapeze_numpy(x_min, x_max, polynome, n)', globals=globals(), number=100)
print(f"Trapezes   (NumPy)  : {1000*temps_trapeze_numpy/(100):.6f} ms")

temps_simpson_python = timeit('calculer_simpson_python(x_min, x_max, polynome, n)', globals=globals(), number=100)
print(f"Simpson    (Python) : {1000*temps_simpson_python/(100):.6f} ms")

temps_simpson_numpy = timeit('calculer_simpson_numpy(x_min, x_max, polynome, n)', globals=globals(), number=100)
print(f"Simpson    (NumPy)  : {1000*temps_simpson_numpy/(100):.6f} ms")


#Faire une boucle for avec n qui va de 1 a 1000, et mesurer le temps, stocker valeur dans un tableau puis tracer une courbe
result_moindre_rectangle_python = []
result_moindre_rectangle_numpy = []
result_trapeze_python = []
result_trapeze_numpy = []
result_simpson_python = []
result_simpson_numpy = []
result_n_values = []

# Listes pour stocker les temps d'exécution
temps_moindre_rectangle_python_list = []
temps_moindre_rectangle_numpy_list = []
temps_trapeze_python_list = []
temps_trapeze_numpy_list = []
temps_simpson_python_list = []
temps_simpson_numpy_list = []


for n in range(1, 200):
    resultat1 = calculer_moindre_rectangle_python(x_min, x_max, polynome, n)
    temps = timeit('calculer_moindre_rectangle_python(x_min, x_max, polynome, n)', globals=globals(), number=100)
    result_moindre_rectangle_python.append(resultat1)
    temps_moindre_rectangle_python_list.append(temps/100 * 1000)  # en ms
    
    # Rectangles NumPy
    resultat2 = calculer_moindre_rectangle_numpy(x_min, x_max, polynome, n)
    temps = timeit('calculer_moindre_rectangle_numpy(x_min, x_max, polynome, n)', globals=globals(), number=100)
    result_moindre_rectangle_numpy.append(resultat2)
    temps_moindre_rectangle_numpy_list.append(temps/100 * 1000)
    
    # Trapèzes Python
    resultat3 = integrale_trapeze_python(x_min, x_max, polynome, n)
    temps = timeit('integrale_trapeze_python(x_min, x_max, polynome, n)', globals=globals(), number=100)
    result_trapeze_python.append(resultat3)
    temps_trapeze_python_list.append(temps/100 * 1000)
    
    # Trapèzes NumPy
    resultat4 = integrale_trapeze_numpy(x_min, x_max, polynome, n)
    temps = timeit('integrale_trapeze_numpy(x_min, x_max, polynome, n)', globals=globals(), number=100)
    result_trapeze_numpy.append(resultat4)
    temps_trapeze_numpy_list.append(temps/100 * 1000)
    
    # Simpson Python
    resultat5 = calculer_simpson_python(x_min, x_max, polynome, n)
    temps = timeit('calculer_simpson_python(x_min, x_max, polynome, n)', globals=globals(), number=100)
    result_simpson_python.append(resultat5)
    temps_simpson_python_list.append(temps/100 * 1000)
    
    # Simpson NumPy
    resultat6 = calculer_simpson_numpy(x_min, x_max, polynome, n)
    temps = timeit('calculer_simpson_numpy(x_min, x_max, polynome, n)', globals=globals(), number=1)
    result_simpson_numpy.append(resultat6)
    temps_simpson_numpy_list.append(temps * 1000)
    
    result_n_values.append(n)

    

# DataFrame pandas avec les résultats
df_resultats = pd.DataFrame({
    'n': result_n_values,
    'Rectangles Python': result_moindre_rectangle_python,
    'Rectangles NumPy': result_moindre_rectangle_numpy,
    'Trapèzes Python': result_trapeze_python,
    'Trapèzes NumPy': result_trapeze_numpy,
    'Simpson Python': result_simpson_python,
    'Simpson NumPy': result_simpson_numpy
})

#  DataFrame pandas avec les temps
df_temps = pd.DataFrame({
    'n': result_n_values,
    'Temps Rectangles Python (ms)': temps_moindre_rectangle_python_list,
    'Temps Rectangles NumPy (ms)': temps_moindre_rectangle_numpy_list,
    'Temps Trapèzes Python (ms)': temps_trapeze_python_list,
    'Temps Trapèzes NumPy (ms)': temps_trapeze_numpy_list,
    'Temps Simpson Python (ms)': temps_simpson_python_list,
    'Temps Simpson NumPy (ms)': temps_simpson_numpy_list
})
'''


def calculer_methode_analytique(f, inf, sup):
    """Valeur exacte de l'integrale du polynome a + b*x + c*x^2 + d*x^3."""
    a,b,c,d=f.coeff
    F_sup = a*sup + b*(sup**2)/2 + c*(sup**3)/3 + d*(sup**4)/4
    F_inf = a*inf + b*(inf**2)/2 + c*(inf**3)/3 + d*(inf**4)/4
    return F_sup - F_inf

def mesurer_temps(fonction, x_min, x_max, polynome, n):
    temps = timeit(lambda: fonction(x_min, x_max, polynome, n), number=100)    
    return temps