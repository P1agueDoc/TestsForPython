grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list1=list(students)

dict_vowels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
student_list=[]
for word1 in dict_vowels:
    for vowel_check in students_list1:
        if word1==vowel_check[0]:
            student_list.append(vowel_check)
            break
        else:
            continue
# Я знаю, что мог сделать так:
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students=sorted(list(students))
student_grades_Sheet=[]
for num1 in grades:
    num_len=len(num1)
    num_zero=0
    for num in num1:
        num_zero=num_zero+num
        continue
    num_end=num_zero/num_len
    student_grades_Sheet.append(num_end)
answer={}
students_len=len(students)
zero1=0
for i1 in range(students_len):
    i1 = {student_list[zero1]: student_grades_Sheet[zero1]}
    zero1=zero1+1
    answer.update(i1)
    continue
print(answer)