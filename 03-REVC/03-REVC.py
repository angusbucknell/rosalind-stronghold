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
