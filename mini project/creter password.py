import random
import string
title = string.ascii_letters
symbols = '!@#$%^&*()_+/*-+?><:}{[];~'
numbers = '0123456789'
all = title + symbols + numbers
while True:
    print('choose an options:\n\t1)Create a Password\n\t2)Exit')
    choice = input('Your choice: ')
    if choice == '1':
        length = int(input('enter the length of password: '))
        password = ''.join((random.sample(all,length)))
        print(password)
    elif choice == '2':
        break
    else:
        print('Your choice is wrong!\n')