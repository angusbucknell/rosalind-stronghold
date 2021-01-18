# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

n = int(input("Number of months: "))
m = int(input("Life expectancy (in months): "))
immature = 1
breeding = 0
pop = [[0,1]]
for x in range(1,n):
    temp = immature
    immature = breeding
    if x > m-1:
        breeding = (breeding) + temp - pop[x-m][1]
    else:
        breeding = breeding + temp
    pop.append([breeding, immature])
print(pop[n-1][0]+pop[n-1][1])
