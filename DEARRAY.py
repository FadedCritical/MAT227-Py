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

output = fact(e)

for i in range(e):
    if(i % 2 == 0):
        output -= comb(e, i + 1) * fact(e - (i + 1))
    else:
        output += comb(e, i + 1) * fact(e - (i + 1))

print(output)