list1=[]
first=input("Enter first: ")
list1.append(first)
second=input("Enter second: ")
list1.append(second)
third=input("Enter third: ")
list1.append(third)
if list1[0] == list1[1] and list1[0] == list1[2]:
    print("3")
elif list1[0] == list1[1] or list1[0] == list1[2]:
    print("2")
elif list1[0] != list1[1] and list1[0] != list1[2]:
    print("0")
else:
    print("Wow, such emptiness")