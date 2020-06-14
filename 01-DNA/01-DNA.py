# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

s = input("Input DNA string: ")
print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))
