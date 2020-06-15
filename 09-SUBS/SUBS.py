# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

s = input("Input string: ")
t = input("Input substring: ")
i = -1
empty = False

while empty == False:
    i = s.find(t,i+1)
    if i == -1:
        empty = True
    else:
        print(i+1, end=" ")
