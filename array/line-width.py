s = "L7. In the codi test I was asked to implement Wrap Text algorithm. Given a long string and a line width, modify the string to put new line so that a line has at most line width amount of character and no line break is given in the middle of a word. (Complete)"


sa = s.split(" ")
lw = 15
i = 0
while i<len(sa):
    lw = 15
    while lw>0:
        
        if i==len(sa):
            break
        lw -=len(sa[i])
        if lw<0:
            break
        print(sa[i], end="")
        i +=1
        if i in range(len(sa)) and lw-len(sa[i])+1 >-1:
            print("", end=" ")
            lw -=1

    print()
"""

sLen = len(s)
i = 0

while i<sLen:
    lw = 15
    while lw:
        print(s[i:i+15])"""

        