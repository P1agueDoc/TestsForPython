def password(first_num):
    num_pass = ""
    for pass_find_check in range(1,first_num):
        for pass_find_check_2 in range(pass_find_check + 1, first_num):
            if first_num % (pass_find_check + pass_find_check_2) == 0:
                num_pass += (str(pass_find_check) + str(pass_find_check_2))

    print(f"{first_num} - {num_pass}")

for i in range(3,21):
    password(i)

# 9 - 1218273645