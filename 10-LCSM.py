FASTA_input = open("rosalind_lcsm.txt", "r")
data = FASTA_input.read().split(">")[1:]

for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]

print(data)


##for k in range(1, len(data)-1):
##    for x in range(0, len(data[0][1])):
##        i = x
##        search = data[0][1][x:i+1]
