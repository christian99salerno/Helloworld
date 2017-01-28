import math

a=input("Inserisci a ")#coefficiente del termine con la x^2
b=input("Inserisci b ")#coefficiente del termine con la x
c=input("Inserisci c ")#termine noto

# ax^2+bx+c=0
delta=b**2-4*a*c


if delta>0:
  x1=(-b+math.sqrt(delta))/2*a
  x2=(-b-math.sqrt(delta))/2*a
  print "L'equazione ha 2 soluzioni:",x1,"e",x2

elif delta==0:
    x=-b/2*a
    print "L'equazione ha 1 soluzione:",x

else:    
    print "L'equazione non ammette soluzioni"

