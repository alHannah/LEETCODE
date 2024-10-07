candies = [2, 3, 5, 1, 3]
extraCandies = 3

maxC = max(candies)

for i in range(len(candies)):
    if candies[i] + extraCandies >= maxC:
        candies[i] = True
    else:
        candies[i] = False
        
print(candies)
    