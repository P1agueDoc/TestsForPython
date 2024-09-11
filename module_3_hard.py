def calculate_structure_sum(data_structure):
    data_structure = str(data_structure)
    counted = 0
    index_num = -1
    skip = 0
    for i in data_structure:
        index_num += 1
        if skip > 0:
            skip -= 1
            continue
        if i.isalpha():
            counted += 1
        elif i.isnumeric():
            if data_structure[index_num+1].isnumeric():
                counted += int(str(i) + str(data_structure[index_num+1]))
                skip += 1
            elif data_structure[index_num-1].isalpha():
                counted += 1
            else:
                counted += int(i)
    return counted



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))