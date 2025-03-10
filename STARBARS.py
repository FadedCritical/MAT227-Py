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

i = int(input("Items: "))
s = int(input("Stars: "))
b = int(input("Bars: "))

if (i != 0):
    print(comb(i + s, b - 1))
else:
    print(comb(s + b, b))