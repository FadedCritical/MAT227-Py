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

s = int(input("Stars: "))
b = int(input("Bars: "))
limit = int(input("Item Limit: ")) + 1

starbars = s + b
output = comb(starbars, b)
if limit - 1 > 0 :
    for i in range(limit-2):
        if(i % 2 == 0):
            output -= comb(b + 1, i + 1) * comb((starbars) - (limit * (i + 1)), b)
        else:
            output += comb(b + 1, i + 1) * comb((starbars) - (limit * (i + 1)), b)
    print(output)
elif limit - 1 == 0:
    itemsPerDistribution = int(input("Items per Distribution: "))
    i = 0
    while(starbars - (itemsPerDistribution + 1) >= b):
        starbars -= itemsPerDistribution + 1
        if(i % 2 == 0):
            output -= comb(b + 1, i + 1) * comb(starbars, b)
        elif(i % 2 == 1):
            output += comb(b + 1, i + 1) * comb(starbars, b)
        i += 1
    print(output)