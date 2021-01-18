# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

s = "AUGCUACUCGGAUCAUUCAGGCUUAUUCCAAAAGAGACUCUAAUCCAAGUCGCGGGGUCAUCCCCAUGUAACCUGAGUUAGCUACAUGGCU"
#open("rosalind_prot.txt","r").read()
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
for x in range(0, len(s), 3):
    codons.append(s[x:x+3])
print(codons)
for y in range(0, len(codons)-1):
    print(translation[codons[y]], end="")

