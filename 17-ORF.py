#Given: A DNA string s of length at most 1 kbp in FASTA format.
#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

#Not too happy with this one - too many lists, and doesn't actually incorporate FATSA file scraping
#However it does pass the challenge - will come back to it some other time
import re

DNAseq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
RNAarr = []
NegRNAarr = []
#Transription of the positive-sense RNA strand
for x in DNAseq:
    if x == "T":
        RNAarr.append("U")
    else:
        RNAarr.append(x)
RNAseq = "".join(RNAarr)

#Trancription of the negative-sense RNA strand
for x in RNAseq[::-1]: #s[::-1] reverses s
    if x == "A":
        NegRNAarr.append("U")
    elif x == "U":
        NegRNAarr.append("A")
    elif x == "C":
        NegRNAarr.append("G")
    elif x == "G":
        NegRNAarr.append("C")
NegRNAseq = "".join(NegRNAarr)

#Setting up codon table for translation
start_pos = []
neg_start_pos = []
codons = []
neg_codons = []
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

#Finds positions of start codons for all positive-sense ORFs
starts = list(re.finditer("(?=AUG)", RNAseq))
for i in range(0, len(starts)):
    start_pos.append(starts[i].start()+1)
#Finds positions of start codons for all negative-sense ORFs
starts = list(re.finditer("(?=AUG)", NegRNAseq))
for i in range(0, len(starts)):
    neg_start_pos.append(starts[i].start()+1)

openORFs = []

#Finds all open-ended +ve ORFs (ie from start AUG to end of string (no stop codons)
for i in range(0, len(start_pos)):
    for j in range(start_pos[i]-1, len(RNAseq), 3):
        codons.append(RNAseq[j:j+3])
    openORFs.append(codons)
    codons = []

#Finds all open-ended -ve ORFs (ie from start AUG to end of string (no stop codons)
for i in range(0, len(neg_start_pos)):
    for j in range(neg_start_pos[i]-1, len(NegRNAseq), 3):
        codons.append(NegRNAseq[j:j+3])
    openORFs.append(codons)
    codons = []

#Translates ORFs into AAs/STOPs
#Translation stops when first STOP is hit, STOP is inc. within AA sequence
ORFs = []
currentORF = []
for x in range(0, len(openORFs)):
    for y in range(0, len(openORFs[x])):
        if translation[openORFs[x][y]] == "STOP":
            currentORF.append("STOP")
            break
        else:
            currentORF.append(translation[openORFs[x][y]])
    ORFs.append(currentORF)
    currentORF = []
    
finalORFs = []
#If the ORF has STOP at the end, it is cleaved off & appended to final list
#If the ORF has no STOP (occurs only in final ORF) it is removed
for k in range(0, len(ORFs)):
    if ORFs[k][-1] == "STOP":
        finalORFs.append("".join(ORFs[k][:-1]))
for x in list(set(finalORFs)):
    print(x)


