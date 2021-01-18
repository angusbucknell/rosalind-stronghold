# Given: Three positive integers representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele. Assume that any two organisms can mate.

k = int(input("Input homozygous dominant: "))
m = int(input("Input heterozygous: "))
n = int(input("Input homozygous recessive: "))
pop = k + m + n

# Calculates probability of BBxBB
k_k = (k/pop) * ((k-1)/(pop-1))
# Calculates probability of BbxBb
# Only 3/4 genotypes contain B
m_m = (m/pop) * ((m-1)/(pop-1)) * 0.75
# Calculates probability of BBxBb
k_m = (k/pop) * (m/(pop-1))
# Calculates probability of BBxbb
k_n = (k/pop) * (n/(pop-1))
# Calculates probability of Bbxbb
# Only 2/4 genotypes contain B
m_n = (m/pop) * (n/(pop-1)) * 0.5

# Calculates all possible pathways leading to genotype w/ B
# Last 3 repeated as they can also be: m_k, n_k, and n_m
prob = k_k + m_m + (2 * k_m) + (2 * k_n) + (2 * m_n)
print(prob)
