FASTA_input = open("rosalind_lcsm.txt", "r")
data = FASTA_input.read().split(">")[1:]

for x in range(0,len(data)):
    data[x] = data[x].splitlines()
for x in range(0,len(data)):
    data[x][1] = "".join(data[x][1:])
    data[x] = data[x][0:2]

print(data)




##for x in range(0,len(data[0][1])):
##    i = x
##    search = data[0][1][x:i+1]
##    print(search)
##    
##    for k in range(1,len(data)-1):
##        if search in data[k][1]:
##            print("Found")
##            i = i + 1
##        else:
##            break
##answer = ""
##for x in range(0,len(data[0][1])):
##    lost = False
##    i = x
##
##    while lost == False and i <= len(data[0][1]):
##        search = data[0][1][x:i+1]
##        print(x,i)
##        print(search)
##        found = 0
##        for k in range(1,len(data)):
##            if search in data[k][1]:
##                print("Found")
##                found = found + 1
##                i = i + 1
##            else:
##                print("Not found")
##                lost = True
##        if found == len(data)-1:
##            if len(search) > len(answer):
##                print("Changing answer to, ", search)
##                answer = search
##print(answer)
##            
##            
##

