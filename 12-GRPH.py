# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

FASTA_input = open("rosalind_grph.txt", "r")
data = FASTA_input.read().split(">")[1:]
# Converts FASTA format to array
for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]

for x in range(0,len(data)):
    temp = data[:]
    del temp[x]
    for y in range(0,len(temp)):
        if data[x][1][-3:] == temp[y][1][:3]:
            print(data[x][0], temp[y][0])
