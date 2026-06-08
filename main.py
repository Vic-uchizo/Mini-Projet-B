from graph import tracer_tous_les_graphiques, methodes
from performance import calculer_methode_analytique, mesurer_temps


def menu_console():
    print("=" * 60)
    print("        SIMULATION D'INTÉGRATION NUMÉRIQUE        ")
    print("=" * 60)
    
    try:
        # 1. Saisie du polynôme
        print("\nSaisie du polynôme :")
        a = float(input("-> Entez a : "))
        b = float(input("-> Entez b : "))
        c = float(input("-> Entez c : "))
        d = float(input("-> Entez d : "))

        def polynome(x):
            """Fonction a integrer : un polynome de 3e ordre."""
            return a + b * x + c * x**2 + d * x**3
        
        polynome.coeff = [a,b,c,d] # Pour facilement recuperer les coefficient dans les fonctions

        # 2. Saisie des bornes
        print("\nSaisie des bornes d'intégration :")
        x_min = float(input("-> Borne minimale (x_min) : "))
        x_max = float(input("-> Borne maximale (x_max) : "))
        
        if x_min >= x_max:
            print("Erreur : x_min doit être inférieur à x_max.")
            return

        # Dictionnaire {nom: fonction} pour retrouver les methodes par leur nom.
        methodes_par_nom = dict(methodes)
        # Familles a comparer : (libelle, nom version Python, nom version NumPy).
        familles = [
            ("Rectangles", "Rectangles (Python)", "Rectangles (NumPy)"),
            ("Trapezes",   "Trapezes (Python)",   "Trapezes (NumPy)"),
            ("Simpson",    "Simpson (Python)",    "Simpson (NumPy)"),
        ]

        # 3. Boucle de choix d'action
        while True:
            print("\n" + "-" * 40)
            print("QUE VEUX-TU FAIRE ?")
            print("1. Afficher les résultats des méthodes (n = 100)")
            print("2. Générer et afficher les 3 graphiques")
            print("3. Comparer les temps Python vs NumPy (tableau)")
            print("4. Quitter")
            choix = input("-> Ton choix (1, 2, 3 ou 4) : ").strip()

            if choix == "1":
                n_test = 100
                print(f"\nCalcul des resultats pour n = {n_test}...\n")
                print(f"Résultat parfait : {calculer_methode_analytique(polynome, x_min, x_max):.2e} \n")
                print(f"{'Méthode':<25} | {'Résultat':<15}")
                print("-" * 45)
                for nom, fonction in methodes:
                    result = fonction(x_min, x_max, polynome, n_test)
                    print(f"{nom:<25} | {result:.2e}")

            elif choix == "2":
                # Lance ton script avec plt.show()
                tracer_tous_les_graphiques(polynome, x_min, x_max)

            elif choix == "3":
                n_test = 1000
                print(f"\nMesure des temps avec timeit pour n = {n_test} (moyenne sur 100 executions)...\n")
                entete = f"{'Méthode':<12} | {'Python (ms)':>12} | {'NumPy (ms)':>12} | {'Accélération':>13}"
                print(entete)
                print("-" * len(entete))
                for libelle, nom_py, nom_np in familles:
                    t_py = mesurer_temps(methodes_par_nom[nom_py], x_min, x_max, polynome, n_test) * 1000
                    t_np = mesurer_temps(methodes_par_nom[nom_np], x_min, x_max, polynome, n_test) * 1000
                    acceleration = t_py / t_np if t_np > 0 else float("inf")
                    print(f"{libelle:<12} | {t_py:>12.4f} | {t_np:>12.4f} | {acceleration:>12.1f}x")
                print("\n-> NumPy est d'autant plus avantageux que n est grand.")

            elif choix == "4":
                print("\nFin du programme. Bye !")
                break
            else:
                print("Choix invalide, tape 1, 2, 3 ou 4.")

    except ValueError:
        print("Erreur de saisie : assure-toi d'entrer des nombres valides.")

if __name__ == "__main__":
    menu_console()