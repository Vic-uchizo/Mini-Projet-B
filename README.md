# Mini-Projet B — Analyse numérique : intégration

**Cours :** MGA802 — Introduction à la programmation avec Python
**Équipe :** *Nnio Kilian Victor*

## Description du projet

Ce projet calcule l'aire sous la courbe d'une fonction polynomiale de 3ᵉ ordre

$$f(x) = p_1 + p_2 x + p_3 x^2 + p_4 x^3$$

à l'aide de plusieurs méthodes d'intégration numérique, puis compare leur
**précision** (erreur par rapport à la solution analytique) et leur
**temps d'exécution**. L'objectif est de démontrer l'avantage de la
vectorisation avec **NumPy** par rapport au Python de base.

Méthodes implémentées :
- **Rectangles** (point milieu) — Python de base et NumPy
- **Trapèzes** — Python de base et NumPy
- **Simpson** — Python de base et NumPy
- **Méthodes pré-programmées** (SciPy : `scipy.integrate`) — référence

## Structure du projet
A COMPLETER

*(Adapter les noms de fichiers selon votre organisation finale.)*

## Prérequis

- Python 3.x
- `numpy`
- `matplotlib`
- `scipy`
- `timeit`, `time` (bibliothèque standard)

Installation des dépendances :

```bash
pip install numpy matplotlib scipy
```

## Utilisation

```bash
python main.py
```

Le programme :
1. fixe les paramètres du polynôme et les bornes d'intégration `[a, b]` ;
2. calcule la solution analytique exacte ;
3. applique chaque méthode d'intégration pour différents nombres de segments `n` ;
4. mesure l'erreur et le temps d'exécution de chaque méthode ;
5. affiche les graphiques de convergence et de performance.

## Fonctions principales

*(à compléter au fur et à mesure du développement)*

| Fonction | Rôle |
|----------|------|
| `solution_analytique(...)` | Calcule la valeur exacte de l'intégrale |
| `rectangles_python(...)` / `rectangles_numpy(...)` | Méthode des rectangles |
| `trapezes_python(...)` / `trapezes_numpy(...)` | Méthode des trapèzes |
| `simpson_python(...)` / `simpson_numpy(...)` | Méthode de Simpson |
| `erreur(...)` | Écart entre valeur numérique et valeur exacte |

## Résultats

*(à compléter : résumé des observations — impact du nombre de segments sur*
*l'erreur et le temps, comparaison des méthodes, gain apporté par NumPy.*
*Les graphiques détaillés et l'analyse se trouvent dans le rapport PDF.)*
