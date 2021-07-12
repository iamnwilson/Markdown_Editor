# read animals.txt
# and write animals_new.txt
with open('animals.txt', 'r') as file1:
    with open('animals_new.txt', 'w') as file2:
        for line in file1:
            file2.write(str(line.replace('\n', ' ')))
