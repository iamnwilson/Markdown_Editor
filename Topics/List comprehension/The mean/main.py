string = input()
new_list = [float(num) for num in string]
print(sum(new_list) / len(string))
