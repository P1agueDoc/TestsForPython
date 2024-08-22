numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for checked_num in numbers:
    is_prime = True
    if checked_num == 1:
        continue
    else:
        for checking in range(2, checked_num):
            if checked_num % checking == 0:
                is_prime = False
                break
            else:
                continue
    if is_prime == True:
        primes.append(checked_num)
    else:
        not_primes.append(checked_num)
print(primes)
print(not_primes)

