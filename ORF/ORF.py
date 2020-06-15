FASTA_input = open("rosalind_orf.txt", "r")
data = FASTA_input.read().split(">")[1:]
# Converts FASTA format to array
for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
starts = []
data[0][1] = data[0][1].replace("T","U")
print(data)

translation = {"UUU":"F", "UUC":"F",
          "UUA":"L", "UUG":"L",
          "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
          "UAU":"Y", "UAC":"Y",
          "UAA":"STOP", "UAG":"STOP", "UGA":"STOP",
          "UGU":"C", "UGC":"C",
          "UGG":"W",
          "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
          "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
          "CAU":"H", "CAC":"H",
          "CAA":"Q", "CAG":"Q",
          "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
          "AUU":"I", "AUC":"I", "AUA":"I",
          "AUG":"M",
          "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
          "AAU":"N", "AAC":"N",
          "AAA":"K", "AAG":"K",
          "AGU":"S", "AGC":"S",
          "AGA":"R", "AGG":"R",
          "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
          "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
          "GAU":"D", "GAC":"D",
          "GAA":"E", "GAG":"E",
          "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

last = 0
finished = False
while finished == False:
    found = (data[0][1].find("AUG",last+1))
    if found != -1:
        starts.append(found)
        last = found
    else:
        finished = True
print(starts)

for x in range(0,len(starts)):
    temp = []
    for y in range(starts[x], len(data[0][1]),3):
        if (data[0][1][y:y+3] == "UAA") or (data[0][1][y:y+3] == "UAG") or (data[0][1][y:y+3] == "UGA"):
            break
        else:
            temp.append(data[0][1][y:y+3])
    print(temp)
    
