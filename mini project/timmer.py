import time
from os import system, name

while True:
    choice = input('do you want to start? (y/n): ')
    if 'y' in choice.lower():
        hour = int(input('enter amount of hour: '))
        minutes = int(input('enter amount of minutes: '))
        seconds = int(input('enter amount of seconds: '))
        total = hour*3600 + minutes*60 + seconds
        print('Timer starting now...')
        time.sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            time.sleep(1)
            if name == 'nt':
                system('cls')
            else:
                system('clear')
        print('Timer ended...')
    elif 'n' in choice.lower():
        print('Exiting...')
    else:
        print('Invalid input...')