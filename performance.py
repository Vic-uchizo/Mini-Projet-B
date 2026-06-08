from timeit import timeit

def calculer_methode_analytique(f, inf, sup):
    """Valeur exacte de l'integrale du polynome a + b*x + c*x^2 + d*x^3."""
    a,b,c,d=f.coeff
    F_sup = a*sup + b*(sup**2)/2 + c*(sup**3)/3 + d*(sup**4)/4
    F_inf = a*inf + b*(inf**2)/2 + c*(inf**3)/3 + d*(inf**4)/4
    return F_sup - F_inf

def mesurer_temps(fonction, x_min, x_max, polynome, n):
    nb_executions = 100
    temps_total = timeit(lambda: fonction(x_min, x_max, polynome, n), number=nb_executions)
    return temps_total / nb_executions  # temps moyen d'UNE execution (en secondes)

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