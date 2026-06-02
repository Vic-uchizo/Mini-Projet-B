### Module de programmation de la methode des moindres carres###
## Fonction de type p1 + p2*x+p3*x^2 +p4*x^3 ###
##inter


a=10
b=50

def polynome(x):
    a=12
    b=13
    c=14
    d=15
    return a+b*x+c*x**2+d*x**3

def calculer_moindre_rectangle_python(a,b,n):
    largeur_segment=b-a/n
    hauteur_segment=[]
    Aire_rectangle_tot=0
    i=a
    while i<=b:
        hauteur_segment=(polynome(i)+polynome(i+largeur_segment))/2
        Aire_rectangle_tot+=largeur_segment*hauteur_segment
        i=i+largeur_segment
    return Aire_rectangle_tot


print(calculer_moindre_rectangle_python(a,b,10))
