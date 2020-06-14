# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs.

n = int(input("Input number of months: "))
k = int(input("Input number of produced litters: "))
breeding = 0
immature = 1
for x in range(0, n):
    temp = immature
    # Simulates new offspring from breedable rabbits
    immature = k * breeding
    # Changes last month immature in breedable rabbits
    breeding = breeding + temp
print(breeding)
