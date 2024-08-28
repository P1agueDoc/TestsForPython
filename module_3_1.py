calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string1):
    string_len = len(string1)
    string_upper = string1.upper()
    string_lower = string1.lower()
    tuple1 = (string_len, string_upper, string_lower)
    count_calls()
    return tuple1


def is_contains(string2, list1):
    count_calls()
    string2 = string2.lower()
    list1_low = []
    for i in list1:
        i = i.lower()
        list1_low.append(i)
    if string2 in list1_low:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
