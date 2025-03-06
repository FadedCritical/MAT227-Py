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

def LaticePath(x1,y1,x2,y2):
    x = x2-x1
    y = y2-y1+x
    return int(comb(y,x))

def PassThru(x1,y1,x2,y2,x3,y3):
    return LaticePath(x1,y1,x2,y2) * LaticePath(x2,y2,x3,y3)

def AvoidPath(x1,y1,x2,y2,x3,y3):
    return LaticePath(x1,y1,x3,y3) - PassThru(x1,y1,x2,y2,x3,y3)

choice = input("\n 1. Lactice Path\n 2. Pass Thru\n 3. Avoid Path\n")

x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

if(choice == "1"):
    print(LaticePath(x1,y1,x2,y2))
elif(choice == "2"):
    x3 = int(input("X3: "))
    y3 = int(input("Y3: "))
    print(PassThru(x1,y1,x2,y2,x3,y3))
elif(choice == "3"):
    x3 = int(input("X3: "))
    y3 = int(input("Y3: "))
    print(AvoidPath(x1,y1,x2,y2,x3,y3))
else:
    print("invalid choice")