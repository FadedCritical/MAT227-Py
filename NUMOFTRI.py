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

m = int(input("How many V-Points: "))
n = int(input("How many H-Points: "))

r = comb(m-1, 1) * comb(n-1, 1)
i = comb(m-1, 1) * comb(n-1, 2) + comb(m-1, 2) * comb(n-1, 1)
t = r + i

print("Right triangles:  %i" % (r))
print("Non-R triangles:  %i" % (i))
print("Total triangles:  %i" % (t))