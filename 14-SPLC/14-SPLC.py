FASTA_input = open("rosalind_splc.txt", "r")
data = FASTA_input.read().split(">")[1:]

for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]
spliced = data[0][1]
for x in range(1,len(data)):
    while spliced.find(data[x][1]) != -1:
        spliced = spliced.replace(data[x][1],"")
r_spliced = spliced.replace("T","U")

codons = []
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
for x in range(0, len(r_spliced), 3):
    codons.append(r_spliced[x:x+3])
for y in range(0, len(codons)-1):
    print(translation[codons[y]], end="")
    
    
