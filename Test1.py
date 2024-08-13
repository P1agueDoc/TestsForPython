#1st program
print(9**0.5*5)

#2nd program
print(9.99>9.98 and 1000 != 1000.1)

#3rd program
a=2*2+2
b=2*(2+2)
print(a)
print(b)
print(a==b)

#4th program
a1='123.456'
def nextDigitAfterDot (numbers):
    numbers_1=numbers
    a_num=0
    for num_check in numbers_1:
        a_num = a_num + 1
        if num_check != '.':
            continue
        else:
            a_dotPlace = (a_num)
            return a_dotPlace
print(a1[int(nextDigitAfterDot(a1))])

#4th program (like it should look like i suppose)
numbers='123.456'
numbers_int_mov=float(numbers)*10
print(int(numbers_int_mov%10))
