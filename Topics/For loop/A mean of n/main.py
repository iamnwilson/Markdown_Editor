num = int(input())
numbers = []
for _ in range(num):
    numbers.append(int(input()))
    
total = sum(numbers)
    
result = total / (len(numbers))
    
print(float(result))
