word = input()
counter = 0
new_word = ""

for char in word:
    if not(char.islower()) and counter > 0:
        new_word = new_word + '_' + char.lower()
    else:
        new_word = new_word + char.lower()
    counter += 1

print(new_word)
