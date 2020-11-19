FASTA_input = open("rosalind_sseq.txt", "r")
data = FASTA_input.read().split(">")[1:]

for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
s = data[0][1]
t = data[1][1]

temp = 0 
for i in range(0, len(t)):
    index = s.index(t[i], temp+1)
    arr.append(index+1)
    temp = index
print(*arr)
    
