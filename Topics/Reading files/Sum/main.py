file = open('sums.txt', 'r')
for line in file:
    output = line.split()
    print(int(output[0]) + int(output[1]))
file.close()
