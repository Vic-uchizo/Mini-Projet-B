from trapeze_python import integrale_trapeze_python
from trapeze_numpy import integrale_trapeze_numpy
from simpson import calculer_simpson_numpy,calculer_simpson_python
from moindre_rectangle import calculer_moindre_rectangle_numpy,calculer_moindre_rectangle_python, calculer_methode_analytique
from timeit import timeit

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
