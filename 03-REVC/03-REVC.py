# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement of s.

s = input("Input DNA string: ")
#s[::-1] reverses s
for x in s[::-1]:
    if x == "A":
        print("T", end = "")
    elif x == "T":
        print("A", end = "")
    elif x == "C":
        print("G", end = "")
    elif x == "G":
        print("C", end = "")
