import math
x = 2
y = 3

def add(param1,param2):
    return param1 + param2

print(add(x+y))

if x == y:
    print("They are the same!")
elif x > y:
    print("x is bigger bruh x=",x)
else:
    print("Y is bigger bruh x=",y)
print("--------------while------------")
lst = [1,2,3,4,5,6]
counter = 0
while(counter < len(lst)):
    print("lst[",counter,"]: ", lst[counter])
    counter += 1 #counter = counter + 1
print("------------for range-------------")
for i in range(0,len(lst)):
    print("lst[",i,"]:", lst[i])
print("------------for lst----------")
for i in lst:
    print[i]

print("--------------Recursion-----------")
def lstPrint(lst):
    if(len(lst) < 1):
        return 0
    else:
        print(lst[0])
        lstPrint(lst[1:])

lstPrint(lst)

s1 = "hello"
s2 = "racecar"

def palindrome(s):
    #solution here
    return True or False