my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_num = 0

while index_num < len(my_list):
    if my_list[index_num] >= 0:
        if my_list[index_num] == 0:
            index_num = index_num + 1
        else:
            print(my_list[index_num])
            index_num = index_num + 1
    else:
        break