import math

a=input("Inserisci a ")#coefficiente del termine con la x^2
b=input("Inserisci b ")#coefficiente del termine con la x
c=input("Inserisci c ")#termine noto

if a==0 and b==0 and c==0:
    print "L'equazione e' indeterminata"
elif a==0 and b==0:
    print "L'equazione e' impossibile"
elif a==0:
    x=-c/b
    print "La x vale",x
else:
    delta = (b**2) - (4.0*a*c)
    if delta>=0:
        x1 = ((-b) + math.sqrt(delta)) / (2.0*a)
        x2 = ((-b) - math.sqrt(delta)) / (2.0*a)
        print "I risultati dell'equazione sono",x1, "e",x2
    else:
        print "L'equazione non ha soluzioni"


