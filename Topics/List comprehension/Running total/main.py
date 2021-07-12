numeric = input()

int_list = [int(x) for x in numeric]

final_list = [sum(int_list[0:x:1]) for x in range(1, len(int_list) + 1)]

print(final_list)
