#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.
    
t = input("Input DNA string: ")
for x in t:
    if x == "T":
        print("U", end="")
    else:
        print(x, end="")
