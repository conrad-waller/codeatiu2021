
#racecar
#0123456
print(list(range(10,1,-2)))
def pal1(s):
    firstHalf = ""
    secHalf = ""
    l = len(s)
    l = 1//2

    for i in range(l):
        firstHalf += s[i]

    for j in range(len(s) - 1, l, -1):
        secHalf += s[j]

    return firstHalf == secHalf
def pal(s):
    l = len(s)
    l = l//2

    for i in range(l):
        if(s[i] != s[len(s)-i - 1]):
            return False
    return True

#for loops here
return firstHalf == secHalf