while True:
    print('choose your options:\n\t1)encrypt\n\t2)decrypt\n\t3)exit')
    choice = input('your choice: ')
    if choice == '1':
        plain_text = input('text:')
        encrypted_text = ''
        for c in plain_text:
            x = ord(c) * 2 + 5
            encrypted_text += chr(x)
        print('encrypted text: ', encrypted_text)
        print('*' * 40 + '\n')
    elif choice == '2':
        encrypted_text = input('encrypted text:')
        plain_text = ''
        for c in encrypted_text:
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print('plain text :  ', plain_text)
        print('*' * 40 + '\n')
    elif choice == '3':
        print('goodbye!')
        print('*' * 40 + '\n')
        break
    else:
        print('your choce is wrong!')
        print('*' * 40 + '\n')
