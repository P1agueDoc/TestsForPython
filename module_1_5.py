immutable_var=(1, "Kitsune", True)
print(immutable_var)
#immutable_var[0]=2
#print(immutable_var)
#Не возможно изменить объекты в кортеже, если они не являются изменяемыми по типу списка [1,2,3] or [true, false, "hi"]

mutable_list= [False, 0.34, "Look", 2]
mutable_list[1]="changed"
print(mutable_list)