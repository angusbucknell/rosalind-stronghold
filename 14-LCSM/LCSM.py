# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

FASTA_input = open("rosalind_lcsm.txt", "r")
data = FASTA_input.read().split(">")[1:]

for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
temp = []
solution = []
# Creates array temp - of all possible motifs
for x in range(0,len(data[0][1])):
    for i in range(0,len(data[0][1])+1):
        search = data[0][1][x:i]
        if search != "":
            temp.append(search)
    # Goes through each possible motif
    for y in range(0,len(temp)):
        counter = 0
        # Checks each possible motif to see if it's within other strings
        for z in range(1,len(data)):
            if temp[y] not in data[z][1]:
                break
            else:
                counter += 1
            # Appends to array of actual motifs
            # Only if it has been found in all other strings
            if counter == len(data)-1:
                solution.append(temp[y])
    temp = []
print(len(data))
# Finds largest string
print(max(solution,key=len))
