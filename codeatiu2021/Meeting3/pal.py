# racecar
# 7/2 = 3



def pal(s):
    l = len(s)
    l = l//2
    for i in range(l):
        if(s[i] != s[len(s)-i - 1]):
            return False
    return True

i = input("ENTER a word: ")
print("your word came back as", pal(i) " for the check")