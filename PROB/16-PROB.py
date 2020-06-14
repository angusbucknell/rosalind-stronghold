data = open("rosalind_prob.txt", "r").read().split("\n")
data[1] = data[1].split(" ")
print(data)

GC = (data[0].count("G") + data[0].count("C")) / (len(data[0]))
print(GC)
