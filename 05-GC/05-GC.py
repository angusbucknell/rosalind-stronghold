# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

FASTA_input = open("rosalind_gc.txt", "r")
data = FASTA_input.read().split(">")[1:]

# Converts FASTA format into array
for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
    
current = 0
for x in range(0,len(data)):
    # Calculates GC-content
    temp = (data[x][1].count("G") + data[x][1].count("C")) / (len(data[x][1]))
    # Saves highest GC-content and its index
    if temp > current:
        current = temp
        pos = x
print(data[pos][0])
print(current*100)
