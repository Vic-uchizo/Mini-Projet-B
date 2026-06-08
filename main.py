import numpy as np

# On importe tes fonctions (ajuste le nom du fichier si nécessaire)
from graph import tracer_tous_les_graphiques, methodes, erreur
from performance import polynome

def menu_console():
    print("=" * 60)
    print("        SIMULATION D'INTÉGRATION NUMÉRIQUE (CONSOLE)        ")
    print("=" * 60)
    
    try:
        # 1. Saisie du polynôme
        print("\nSaisie du polynôme :")
        a = int(input("-> Entez a : "))
        b = int(input("-> Entez b : "))
        c = int(input("-> Entez c : "))
        d = int(input("-> Entez d : "))

        polynome.coeffs[a, b, c, d]
        print(f"\nPolynôme configuré :\n{polynome}")
        
        # 2. Saisie des bornes
        print("\nSaisie des bornes d'intégration :")
        x_min = int(input("-> Borne minimale (x_min) : "))
        x_max = int(input("-> Borne maximale (x_max) : "))
        
        if x_min >= x_max:
            print("❌ Erreur : x_min doit être inférieur à x_max.")
            return

        # 3. Boucle de choix d'action
        while True:
            print("\n" + "-" * 40)
            print("QUE VEUX-TU FAIRE ?")
            print("1. Afficher les résultats des méthodes (n = 100)")
            print("2. Générer et afficher les 3 graphiques")
            print("3. Quitter")
            choix = input("-> Ton choix (1, 2 ou 3) : ").strip()

            if choix == "1":
                n_test = 100
                print(f"\nCalcul des erreurs absolues pour n = {n_test}...\n")
                print(f"{'Méthode':<25} | {'Erreur Absolue':<15}")
                print("-" * 45)
                for nom, fonction in methodes:
                    result = fonction(x_min, x_max, polynome, n_test)
                    print(f"{nom:<25} | {result:.2e}")
                    
            elif choix == "2":
                # Lance ton script avec plt.show()
                tracer_tous_les_graphiques(polynome, x_min, x_max)
                
            elif choix == "3":
                print("\nFin du programme. Bye !")
                break
            else:
                print("❌ Choix invalide, tape 1, 2 ou 3.")

    except ValueError:
        print("❌ Erreur de saisie : assure-toi d'entrer des nombres valides.")

if __name__ == "__main__":
    menu_console()