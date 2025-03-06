#Created by
#Ronald Armistead-Tyler
def fact(num):
    if(num==1 or num == 0):
        return 1
    else:
        returnNum = num
        for i in range(num-1): returnNum *= i+1
        return returnNum
w = input("Word: ")
s = list(set(w))
a = []
t = fact(len(w))
for i in range (len(s)):
    if(w.count(s[i]) > 1):
        t /= fact(w.count(s[i]))
print(int(t))