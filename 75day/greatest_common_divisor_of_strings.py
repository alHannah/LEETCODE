import math

str1 = "ABAB"
str2 = "ABABABAB"

list1 = list(str1)
list2 = list(str2)

listLen1 = len(list1)
listLen2 = len(list2)

container = []

if list1 + list2 != list2 + list1:
    print(container)
gcd = math.gcd(listLen1, listLen2)
container = list1[:gcd]

print(''.join(container))
