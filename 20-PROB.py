#Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
#Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

import math
s = list(input("Input DNA sequence: "))
A = input("Input probabilities: ").split(" ")

def probCalc(x):
    prob = 1
    for i in range(0, len(s)):
        if s[i] == "A" or s[i] == "T":
            prob = prob * ((1-x)/2)
        else:
            prob = prob * (x/2)
    return prob


arr = []
for j in range(0, len(A)):
    arr.append(math.log10(probCalc(float(A[j]))))
print(*arr)







