mutation_data = open("rosalind_hamm.txt", "r")
data = mutation_data.read().split("\n")
hamming_distance = 0
for x in range(0, len(data[0])):
    if data[0][x] != data[1][x]:
        hamming_distance = hamming_distance + 1
print(hamming_distance)
