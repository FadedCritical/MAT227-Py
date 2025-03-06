#Created by
#Ronald Armistead-Tyler
def fact(num):
    if(num==1 or num == 0):
        return 1
    else:
        returnNum = num
        for i in range(num-1): returnNum *= i+1
        return returnNum

def comb(y,x):
    return fact(y) / (fact(x) * fact(y-x))

def numOfPara(n,m):
    x = 0
    n -= 1
    for i in range(n): x += pow(i+1, m)
    return x

m = int(input("How many V-Points: "))
n = int(input("How many H-Points: "))
s = int(input("How many are squares: "))

q = comb(n, m) * comb(n, m)
r = comb(n, m) * comb(n, n)
p = numOfPara(n, m)
t = q - p

print("Quadrilaterals:  %i" % (q))
print("Squares:  %i" % (s))
print("Rectangles:  %i" % (r))
print("Parallelograms:  %i" % (p))
print("Trapeziods:  %i" % (q))
print("Trape not para:  %i" % (t))