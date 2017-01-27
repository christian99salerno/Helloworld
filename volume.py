import math
figura=input("Effettua una scelta: (1 - cubo, 2 - sfera) ")
if figura == 1:
    lato=input("lato del cubo: ")
    vol1=lato**3
    print "Il cubo di lato ",lato," ha volume ",vol1
else:
    raggio=input("raggio della sfera: ")
    vol2=(4.0/3.0) * math.pi * (raggio**3)
    print "La sfera di raggio ",raggio," ha volume ",vol2
