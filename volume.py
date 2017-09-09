import math
print "Calcolo del volume di un cubo o di una sfera"
figura=input("Effettua una scelta: (1 - cubo, 2 - sfera)? ")
if figura == 1:
    lato=input("lato del cubo: ")
    vol=lato**3
    print "Il cubo di lato ",lato," ha volume ",vol
else:
    raggio=input("raggio della sfera: ")
    vol=(4.0/3.0) * math.pi * (raggio**3)
    print "La sfera di raggio ",raggio," ha volume ",vol
