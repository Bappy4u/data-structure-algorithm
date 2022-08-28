import string
s = "Hello woreldolee"

dic = {key: 0 for key in s if ord(key) in range(97,123)}
mav = 0
maxc = ["",""]

for char in s:
    if ord(char) in range(97,123):
        dic[char] +=1
        if dic[char]>=mav:
            maxc.pop(0)
            mav = dic[char]
            maxc.append(char)

print(maxc[0])
alphabet_string = {key: 0 for key in string.ascii_lowercase}
print(alphabet_string)








