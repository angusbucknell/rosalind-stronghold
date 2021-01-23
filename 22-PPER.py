import math

n= int(input("Please input n: "))
k= int(input("Please input k: "))

def P(n, k):
    return int(math.factorial(n)/math.factorial(n-k) % 1000000)

print(P(n, k))
    
