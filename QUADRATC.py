#Created by
#Ronald Armistead-Tyler
from math import sqrt, fabs

def quad(a, b, c, x=None):
    if(x==None):
        d = pow(b,2) - 4*a*c
        sol1 = (-b + sqrt(fabs(d))) / (2*a)
        sol2 = (-b - sqrt(fabs(d))) / (2*a)
        return sol1, sol2
    else:
        return a * pow(x, 2) + b * x + c

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
s1, s2 = quad(a, b, c)
x = -b / (2 * a)
y = quad(a, b, c, x)
print("Zeros: %f, %f" % (s1, s2))
print("Vertex: (%f,%f)" % (x, y))