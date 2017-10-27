import itertools
max_length = 10
name = input("Enter the initial string: ")  # This should have minimum value 3
if len(name) < 3:
    print("file created is so big, Try again with big string.")
    exit(code=7)
password_file = name + "_password.txt"
number_of_passwords = 0
f = open(password_file, "w")
max_digit_length = max_length - len(name)
digit_length = 1
digit_string = ""
while digit_length <= max_digit_length:
    per_obj = itertools.product(range(10), repeat=digit_length)
    for i in per_obj:
        for digit in i:
            digit_string = digit_string + str(digit)
        s = name + digit_string + "\n"
        f.write(s)
        number_of_passwords += 1
        if number_of_passwords % 5000 == 0:
            print(s)
        digit_string = ""
    digit_length += 1

print("Password file of name ", password_file, " is created.")
print("It contains", number_of_passwords, " passwords")
f.close()
