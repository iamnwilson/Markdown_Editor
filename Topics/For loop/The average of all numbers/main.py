# put your python code here
a = int(input())
b = int(input())
low_range = a
high_range = b + 1
count = 0
total = 0

for i in range(low_range, high_range, 1):
    if i % 3 == 0:
        total += i
        count += 1
    elif i % 3 != 0:
        pass
print(total / count)
