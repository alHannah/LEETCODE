import math

print(math.gcd(6, 6)) 

str1 = "ABCDEF"
str2 = "ABCABC"

list1 = list(str1)
list2 = list(str2)

listLen1 = len(list1)
listLen2 = len(list2)

if list1 + list2 != list2 + list1:
    print("")
gcd = math.gcd(listLen1, listLen2)
print(list1[:gcd])
print(list1)
print(gcd)
