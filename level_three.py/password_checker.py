
digit, upper, char, letter = False, False, False, False
pw_valid = False
counter = 0

while not pw_valid:
    pw = input("Enter pw:")

    for i in pw:
        if i.isupper():
            upper = True
        elif i.isdigit():
            digit = True
        elif i in "!@£$%^&*":
            char=True
        elif i.islower():
            letter=True
        else:
            pass

        counter+=1

        if char and digit and char and letter:
            pw_valid=True
            break
        else:
            continue

    if pw_valid:
        print("SUCCESS")
        print(counter)
    else:
        print("TRY AGAIN")