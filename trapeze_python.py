# =============================================================================
# Methode des TRAPEZES, codee en Python de base (sans NumPy)
# =============================================================================
# Objectif : approximer l'aire sous la courbe d'une fonction f sur [a, b].
#
# La fonction a integrer est passee EN PARAMETRE (f). Ainsi ce module est
# generique : il peut integrer n'importe quelle fonction, pas seulement notre
# polynome. C'est main.py qui definit le polynome et le passe a l'appel.
# =============================================================================


def integrale_trapeze_python(a, b, f, n):
   
    # Largeur (constante) de chaque segment.
    h = (b - a) / n

    # On va accumuler l'aire des trapezes dans cette variable.
    aire_totale = 0.0

    # On parcourt les n segments, un par un : i = 0, 1, ..., n-1.
    for i in range(n):
        # Bord gauche et bord droit du segment numero i.
        x_gauche = a + i * h
        x_droite = a + (i + 1) * h

        # Hauteurs du trapeze : valeur de f aux deux bords.
        # On appelle simplement f(...) : peu importe ce qu'est f exactement.
        f_gauche = f(x_gauche)
        f_droite = f(x_droite)

        # Aire d'un seul trapeze (formule 2).
        aire_segment = h * (f_gauche + f_droite) / 2

        # On l'ajoute au total.
        aire_totale += aire_segment

    return aire_totale
