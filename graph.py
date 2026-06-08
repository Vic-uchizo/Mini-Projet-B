# =============================================================================
# Graphiques
# Produit les 3 graphiques demandes dans la consigne (section 2.5) :
#   1. Convergence : erreur en fonction du nombre de segments n
#   2. Performance : temps de calcul en fonction du nombre de segments n
#   3. Erreur en fonction de la methode et du nombre de segments (barres)
#
# Le polynome et les bornes ne sont PAS definis ici car ils sont en
# argument par main.py. On evite ainsi de reecrire le polynome a deux endroits.
# Le temps de calcul est mesure par performance.mesurer_temps.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid, simpson

# Mesure du temps : on reutilise la fonction du fichier du collegue.
from performance import calculer_methode_analytique

# On reutilise les fonctions deja codees dans les autres fichiers.
from trapeze_python import integrale_trapeze_python
from trapeze_numpy import integrale_trapeze_numpy
from simpson import calculer_simpson_python, calculer_simpson_numpy
from moindre_rectangle import (
    calculer_moindre_rectangle_python,
    calculer_moindre_rectangle_numpy
)


# -----------------------------------------------------------------------------
# On utilise les fonctions de base de python pour intégrer pour pouvoir les comparer aux notres
# -----------------------------------------------------------------------------
def scipy_trapeze(inf, sup, f, n):
    x = np.linspace(inf, sup, n + 1)
    return trapezoid(f(x), x)


def scipy_simpson(inf, sup, f, n):
    x = np.linspace(inf, sup, 2 * n + 1)  # nb impair de noeuds pour nombre paire d'intervalles 
    return simpson(f(x), x=x)


# -----------------------------------------------------------------------------
# Liste de l'inventaire des methodes : (nom, fonction)
# -----------------------------------------------------------------------------
methodes = [
    ("Rectangles (Python)", calculer_moindre_rectangle_python),
    ("Rectangles (NumPy)",  calculer_moindre_rectangle_numpy),
    ("Trapezes (Python)",   integrale_trapeze_python),
    ("Trapezes (NumPy)",    integrale_trapeze_numpy),
    ("Simpson (Python)",    calculer_simpson_python),
    ("Simpson (NumPy)",     calculer_simpson_numpy),
    ("Trapezes (scipy)",    scipy_trapeze),
    ("Simpson (scipy)",     scipy_simpson),
]

# Valeurs de n testees (echelle logarithmique : 1, 2, 5, 10, ... 1000).
liste_n = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]


# -----------------------------------------------------------------------------
# Fonctions erreur entre les methodes et la valeur exacte
# -----------------------------------------------------------------------------

def erreur(fonction, polynome, x_min, x_max, n):
    """Ecart absolu entre la methode et la valeur exacte, pour n segments."""
    exacte = calculer_methode_analytique(polynome, x_min, x_max)
    approx = fonction(x_min, x_max, polynome, n)
    return abs(approx - exacte)


# =============================================================================
# GRAPHIQUE 1 : Convergence (erreur en fonction de n)
# =============================================================================
def graphique_convergence(polynome, x_min, x_max):
    plt.figure(figsize=(9, 6))
    for nom, fonction in methodes:
        erreurs = [erreur(fonction, polynome, x_min, x_max, n) for n in liste_n]
        plt.plot(liste_n, erreurs, marker="o", label=nom)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Nombre de segments n")
    plt.ylabel("Erreur absolue")
    plt.title("Convergence : erreur en fonction du nombre de segments")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graphique_convergence.png", dpi=150)
    print("-> graphique_convergence.png enregistre")


# =============================================================================
# GRAPHIQUE 2 : Performance (temps de calcul en fonction de n)
# =============================================================================
def graphique_performance(polynome, x_min, x_max):
    plt.figure(figsize=(9, 6))
    for nom, fonction in methodes:
        temps_mesures = [mesurer_temps(fonction, x_min, x_max, polynome, n) for n in liste_n]
        plt.plot(liste_n, temps_mesures, marker="o", label=nom)

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Nombre de segments n")
    plt.ylabel("Temps de calcul (ms)")
    plt.title("Performance : temps de calcul en fonction du nombre de segments")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graphique_performance.png", dpi=150)
    print("-> graphique_performance.png enregistre")


# =============================================================================
# GRAPHIQUE 3 : Erreur en fonction de la methode et de n (barres groupees)
# =============================================================================
def graphique_erreur_par_methode(polynome, x_min, x_max):
    n_choisis = [10, 50, 200]
    noms = [nom for nom, _ in methodes]
    positions = np.arange(len(noms))
    largeur = 0.25

    plt.figure(figsize=(11, 6))
    for i, n in enumerate(n_choisis):
        erreurs = [erreur(fonction, polynome, x_min, x_max, n) for _, fonction in methodes]
        plt.bar(positions + i * largeur, erreurs, largeur, label=f"n = {n}")

    plt.yscale("log")
    plt.xticks(positions + largeur, noms, rotation=30, ha="right")
    plt.ylabel("Erreur absolue")
    plt.title("Erreur en fonction de la methode et du nombre de segments")
    plt.legend()
    plt.grid(True, axis="y", which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("graphique_erreur_par_methode.png", dpi=150)
    print("-> graphique_erreur_par_methode.png enregistre")


def tracer_tous_les_graphiques(polynome, x_min, x_max):
    """Genere les 3 graphiques puis les affiche."""
    print("Generation des graphiques...")
    graphique_convergence(polynome, x_min, x_max)
    graphique_performance(polynome, x_min, x_max)
    graphique_erreur_par_methode(polynome, x_min, x_max)
    print("Termine.")
    plt.show()
