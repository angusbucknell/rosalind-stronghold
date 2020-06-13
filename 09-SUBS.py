s = input("Input string: ")
t = input("Input substring: ")
i = -1
empty = False

while empty == False:
    i = s.find(t,i+1)
    if i == -1:
        empty = True
    else:
        print(i+1, end=" ")
