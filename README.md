# Mini-Projet B — Intégration numérique

**Cours :** MGA802 — Introduction à la programmation avec Python
**Équipe :** Nino, Kilian, Victor

## Description

Le programme calcule l'aire sous la courbe d'un polynôme de 3ᵉ ordre

$$f(x) = a + b\,x + c\,x^2 + d\,x^3$$

par plusieurs méthodes d'intégration numérique, puis compare leur **précision**
(erreur par rapport à la solution analytique exacte) et leur **temps d'exécution**.
Objectif : montrer le gain apporté par la vectorisation **NumPy** face au Python de base.

Méthodes : **rectangles**, **trapèzes** et **Simpson**, chacune codée en Python de base
puis en NumPy, plus les versions pré-programmées de **SciPy** (`scipy.integrate`) comme référence.

## Prérequis

```bash
pip install numpy matplotlib scipy
```

(`timeit` et `time` font partie de la bibliothèque standard.)

## Utilisation

```bash
python main.py
```

Le programme demande les coefficients `a, b, c, d` du polynôme et les bornes `[x_min, x_max]`,
puis propose un menu :

1. **Résultats des méthodes** (n = 100) — valeur de chaque méthode vs solution exacte
2. **Graphiques** — convergence, temps de calcul et erreur par méthode (enregistrés en `.png`)
3. **Temps Python vs NumPy** — tableau comparatif avec facteur d'accélération
4. **Quitter**

## Structure des fichiers

| Fichier | Contenu |
|---------|---------|
| `main.py` | Point d'entrée : saisie utilisateur et menu |
| `moindre_rectangle.py` | Méthode des rectangles (Python et NumPy) |
| `trapeze_python.py` / `trapeze_numpy.py` | Méthode des trapèzes |
| `simpson.py` | Méthode de Simpson (Python et NumPy) |
| `performance.py` | Solution analytique, calcul d'erreur, mesure du temps (`timeit`) |
| `graph.py` | Méthodes SciPy et génération des 3 graphiques |

Chaque méthode reçoit la fonction `f` en paramètre, les bornes et le nombre de segments `n`.

## Résultats

- L'erreur diminue quand `n` augmente (convergence) ; Simpson est exact pour un polynôme
  de degré ≤ 3, son erreur reste au niveau de la précision machine.
- Les versions **NumPy** sont environ **10 à 15× plus rapides** que le Python de base,
  et l'écart grandit avec `n`.

Analyse détaillée et graphiques dans le **rapport PDF**.
