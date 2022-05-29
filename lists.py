list_A = ['M', 'a', 'n']
list_B = ['W', 'o', 'm', 'a', 'n']
matrix = [list_A, list_B]
print(matrix)

combined = [*list_A, '&', *list_B]
print(combined)

x, y, *z = list_B
print(x, y, z)

num_list = list(range(10))
print(num_list)

for index, num_list in enumerate(num_list):
    print(f'{index}:{num_list}', end=' ~ ')
