#Created by 
#Ronald Armistead-Tyler
def recurrence1(x, y, z, xx):
    result = y

    mult = float(input("Function mult?: "))
    p1 = float(input("mult power?: "))
    add = float(input("Function add?: "))
    p2 = float(input("add power?: "))

    while(x != z):
        x += 1
        result = pow(mult, p1) * pow(result, xx) + pow(add, p2)
        print(result)
        
x = float(input("known f(?): "))
y = float(input("f(%x) = ?:  " % (x)))
z = float(input("solve f(?): "))
xx = float(input("To power of: "))

recurrence1(x, y, z, xx)
