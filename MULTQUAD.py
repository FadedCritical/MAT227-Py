#Created by
#Ronald Armistead-Tyler
from math import ceil
def quad(a, b, c, x):
    return a * pow(x, 2) + b * x + c

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
sX = float(input("X START: "))
eX = float(input("X END: "))
pX = float(input("X PERIODS: "))

x = []
y = []

y.append(round(quad(a, b, c, sX), 4))
for i in range(int(ceil((eX - sX) / pX))):
    x.append(round(sX, 4))
    sX += pX
    y.append(round(quad(a, b, c, sX), 4))
x.append(round(sX, 4))

print("\nX\t\t\t\t Y")
for i in range(len(x)):
    if(i%6 == 5):
        input()
    print("%f\t%f" % (x[i], y[i]))