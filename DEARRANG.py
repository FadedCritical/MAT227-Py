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

e = int(input("How many elements?: "))
n = int(input("How many fixed elements?: "))
ee = e - n
output = 0

if n == 0:
    output = fact(e)
    for i in range(e):
        if(i % 2 == 0):
            output -= comb(e, i + 1) * fact(e - (i + 1))
        else:
            output += comb(e, i + 1) * fact(e - (i + 1))
else:
    output = fact(ee)
    for i in range(ee):
        if(i % 2 == 0):
            output -= comb(ee, i + 1) * fact(ee - (i + 1))
        else:
            output += comb(ee, i + 1) * fact(ee - (i + 1))
    output *= comb(e, n)

print(output)