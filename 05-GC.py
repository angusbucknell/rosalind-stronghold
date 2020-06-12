FASTA_input = open("rosalind_gc.txt", "r")
data = FASTA_input.read().split(">")[1:]

for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
    
current = 0
for x in range(0,len(data)):
    temp = (data[x][1].count("G") + data[x][1].count("C")) / (len(data[x][1]))
    if temp > current:
        current = temp
        pos = x
print(data[pos][0])
print(current*100)
