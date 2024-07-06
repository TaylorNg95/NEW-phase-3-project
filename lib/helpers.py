import subprocess
import ipdb

def clear_screen():
    subprocess.run('clear')

def show_user_error(e=''):
    if e:
        print('')
        print(f'Error: {e}')
        print('')
    else:
        print('')
        print('Invalid input. Please try again!')
        print('')

def check_proceed():
    print('Type "1" to proceed')
    print('Type "2" to return to main menu')
    print('')
    choice = input('Enter selection: ')
    return choice

def exit_program():
    print("Goodbye!")
    ipdb.set_trace()
    exit()
