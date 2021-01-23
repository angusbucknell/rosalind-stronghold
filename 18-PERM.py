import math
from itertools import permutations
arr = []
n = int(input("Input integer n<=7: "))

for i in range(0, n):
    arr.append(str(i+1))

print(int(math.factorial(n)/math.factorial(n-n))) #The nPr formula
for i in permutations("".join(arr)):
    print(" ".join(i))
