# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1,s2).

FASTA_input = open("rosalind_tran.txt", "r")
data = FASTA_input.read().split(">")[1:]
# Converts FASTA format to array
for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]

transversion = 0
transition = 0

for x in range(0,len(data[0][1])):
    if (data[0][1][x] == "A" and data[1][1][x] == "G") or (data[0][1][x] == "G" and data[1][1][x] == "A") or (data[0][1][x] == "C" and data[1][1][x] == "T") or (data[0][1][x] == "T" and data[1][1][x] =="C"):
        transition += 1
    elif (data[0][1][x] == data[1][1][x]):
        pass
    else:
        transversion += 1
print(transition/transversion)
        
