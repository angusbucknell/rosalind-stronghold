# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection.

FASTA_input = open("rosalind_cons.txt", "r")
data = FASTA_input.read().split(">")[1:]
# Converts FASTA format into array
for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]

A = []
C = []
G = []
T = []
A_temp,C_temp,G_temp,T_temp = 0,0,0,0
# Creates matrix as series of arrays
for x in range(0,len(data[0][1])):
    for y in range(0, len(data)):
        if data[y][1][x] == "A":
            A_temp += 1
        elif data[y][1][x] == "C":
            C_temp += 1
        elif data[y][1][x] == "G":
            G_temp += 1
        elif data[y][1][x] == "T":
            T_temp += 1
    A.append(A_temp)
    C.append(C_temp)
    G.append(G_temp)
    T.append(T_temp)
    A_temp,C_temp,G_temp,T_temp = 0,0,0,0
# Creates census string
# Each column mapped as an array
# Which row corresponds to base
consensus = []
for x in range(0,len(A)):
    col = [A[x],C[x],G[x],T[x]]
    if col.index(max(col)) == 0:
        consensus.append("A")
    if col.index(max(col)) == 1:
        consensus.append("C")
    if col.index(max(col)) == 2:
        consensus.append("G")
    if col.index(max(col)) == 3:
        consensus.append("T")
        
print("".join(consensus))
print("A: "," ".join(str(x) for x in A))
print("C: "," ".join(str(x) for x in C))
print("G: "," ".join(str(x) for x in G))
print("T: "," ".join(str(x) for x in T))
