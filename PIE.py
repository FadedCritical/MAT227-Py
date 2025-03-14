#Created by
#Ronald Armistead-Tyler
from math import floor

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
e = int(input("Item Limit: ")) + 1

output = comb(s + b, b)
if e - 1 > 0 : 
    for i in range(e):
        if(i % 2 == 0):
            output -= comb(b + 1, i + 1) * comb((s + b) - (e * (i + 1)), b)
        else:
            output += comb(b + 1, i + 1) * comb((s + b) - (e * (i + 1)), b)
elif e - 1 == 0:
    bins = int(input("Bins: "))
    binVolume = int(input("Items per bin: "))
    if bins > 0:
        for i in range(floor((s + b) / bins) - 1):
            if(i % 2 == 0):
                output -= comb(b + 1, i + 1) * comb((s + b) - ((binVolume + 1) * (i + 1)), b)
            else:
                output += comb(b + 1, i + 1) * comb((s + b) - ((binVolume + 1) * (i + 1)), b)

print(round(output))