# Given: Six integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor.
# 1 = AA-AA (100%)
# 2 = AA-Aa (100%)
# 3 = AA-aa (100%)
# 4 = Aa-Aa (75%)
# 5 = Aa-aa (50%)
# 6 = aa-aa (0%)
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

file = open("rosalind_iev.txt", "r")
data = file.read().split()
prob = 0
for x in range(0, 3):
    # Sums the probabilities of 2 offspring getting A
    prob = prob + (int(data[x]) * 2)
# 5th element ignores as aa-aa cannot produce A
print(prob + (int(data[3]) * 2 * 0.75) + int(data[4]))
