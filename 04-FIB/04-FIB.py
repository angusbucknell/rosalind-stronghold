n = int(input("Input number of months: "))
k = int(input("Input number of produced litters: "))
breeding = 0
immature = 1
for x in range(0, n):
    temp = immature
    immature = k * breeding
    breeding = breeding + temp
print(breeding)
