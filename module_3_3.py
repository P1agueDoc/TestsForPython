def print_params(a = 1, b = 'строка', c = True):
    print(a)
    print(b)
    print(c)

values_list = [1,True,"Yes"]
values_dict = {'a': 4,'b': "good",'c': False}

#print_params(*values_list)
#print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)