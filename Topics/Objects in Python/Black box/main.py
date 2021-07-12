# use the function blackbox(lst) that is already defined
numbers = [3, 2, 1]
new = blackbox(numbers)
if id(numbers) == id(new):
    print("modifies")
else:
    print("new")
