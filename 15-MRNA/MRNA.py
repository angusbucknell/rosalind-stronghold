# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.

file = open("rosalind_mrna.txt", "r")
proteins = list(file.read())
print(proteins)
codons = {'F':2, 'STOP':3, 'G':4, 'R':6, 'P':4, 'S':6, 'M':1, 'W':1, 'A':4, 'Y':2, 'I':3, 'D':2, 'T':4, 'L':6, 'K':2, 'C':2, 'Q':2, 'N':2, 'V':4, 'H':2, 'E':2}
poss = 1
for x in range(0,len(proteins)):
    poss = poss * (codons[proteins[x]])
poss = (poss * 3)%1000000
print(poss)
