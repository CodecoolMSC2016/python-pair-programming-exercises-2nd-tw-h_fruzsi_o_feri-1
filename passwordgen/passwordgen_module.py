import random, string

def passwordgen():
    length = 8
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    password = (''.join(random.choice(chars) for i in range(length)))
    return password


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()
'''

#length = 8
#chars = string.ascii_letters + string.digits + '!@#$%^&*()'
#print(''.join(random.choice(chars) for i in range(length)))

def passwordgen():
    length = 8
    letters = string.ascii_letters
    numbers = string.digits
    special = "!@#$%^&*()"
    #chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    chars = letters + numbers + special
    password = (''.join(random.choice(chars) for i in range(length)))
    print(password)
    #return password
passwordgen()'''