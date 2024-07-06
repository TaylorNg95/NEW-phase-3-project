import subprocess

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

def exit_program():
    print("Goodbye!")
    exit()
