import subprocess
from models.opponent import Opponent

def clear_screen():
    subprocess.run('clear')

def print_header(header):
    print(header)
    print('')

def show_user_error(e=''):
    if e:
        print('')
        print(f'Error: {e}')
        print('')
    else:
        print('')
        print('Invalid selection. Please try again!')
        print('')

def check_proceed():
    print('Type "1" to proceed')
    print('Type "2" to return to main menu')
    print('')
    choice = input('Enter selection: ')
    return choice

def return_to_main_menu(self):
    clear_screen()
    self.options()

def calc_match_spacing(obj):
    # custom spacing for record IDs of differing lengths (formatting purposes only)
    spacing = '  '
    if 10 <= obj.id < 100:
        spacing = ' '
    elif 100 <= obj.id < 1000:
        spacing = ''
    return spacing

def print_match(match, spacing):
    opponent_name = Opponent.all.get(match.opponent_id).name
    print(f'ID: {match.id}{spacing}| DATE: {match.date} | OUTCOME: {"W" if match.outcome == 1 else "L"} | OPPONENT: {opponent_name}')
    print('------')

def print_opponent(opponent, spacing):
    print(f'ID: {opponent.id}{spacing}| {opponent.name}')
    print('------')

def exit_program():
    print("Goodbye!")
    exit()
