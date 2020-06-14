file = open("rosalind_iev.txt", "r")
data = file.read().split()
prob = 0
for x in range(0, 3):
    prob = prob + (int(data[x]) * 2)
print(prob + (int(data[3]) * 2 * 0.75) + int(data[4]))
