FASTA_input = open("rosalind_orf.txt", "r")
data = FASTA_input.read().split(">")[1:]
# Converts FASTA format to array
for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
#print(data[0][1])
rc = ""
for x in data[0][1][::-1]:
    if x == "A":
        rc += "T"
    elif x == "T":
        rc += "A"
    elif x == "C":
        rc += "G"
    elif x == "G":
        rc += "C"

data[0][1] = data[0][1].replace("T","U")
rc = rc.replace("T","U")
print(data[0][1])
print(rc)

starts = []
rc_starts = []

last = 0
finished = False
while finished == False:
    found = (data[0][1].find("AUG",last+1))
    if found != -1:
        starts.append(found)
        last = found
    else:
        finished = True
last = 0
finished = False
while finished == False:
    found = (rc.find("AUG",last+1))
    if found != -1:
        rc_starts.append(found)
        last = found
    else:
        finished = True

print(starts)
print(rc_starts)



