asterisk_string = "*"

space_number = 4
count = 0
while count < 5:
    string_to_print = " "*space_number + asterisk_string
    print(string_to_print)
    asterisk_string += ' *'
    space_number -= 1
    count += 1
