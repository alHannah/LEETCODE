word1 = "abcdefghijklmn"
word2 = "opqrs"

lis1 = list(word1)
lis2 = list(word2)
n = 0

listLen = len(lis1) + len(lis2)
com = []

if len(lis1) <= len(lis2):
    shortList = len(lis1)
    large = lis2
else:
    shortList = len(lis2)
    large = lis1

for i in range(listLen - 1):
    # shortest length
    if i < shortList:
        com.append(lis1[n])
        com.append(lis2[n])
        n += 1
        
    elif n < len(large):
        com.append(large[n])
        n += 1

print(com)
