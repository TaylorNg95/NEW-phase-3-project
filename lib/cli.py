from helpers import (
    clear_screen,
    print_header,
    show_user_error,
    check_proceed,
    calc_match_spacing,
    exit_program
    )
from models.match import Match
from models.opponent import Opponent

class Cli:

    def run(self):
        clear_screen()
        print('WELCOME TO YOUR MATCH LOG!')
        self.options()

    def options(self):
        print('')
        print('Type "1" to view all matches')
        print('Type "2" to add new match')
        print('Type "3" to delete existing match')
        print('Type "4" to view all opponents')
        print('Type "5" to add new opponent')
        print('Type "6" to delete existing opponent')
        print('Type "7" to search matches by opponent')
        print('Type "8" to search matches by date')
        print('Type "exit" to exit program')
        print('')
        self.selection()

    def selection(self):
        sel = input('Enter selection: ')
        clear_screen()
        if sel == '1':
            self.view_all_matches()
        elif sel == '2':
            self.add_new_match()
        elif sel == '3':
            self.delete_existing_match()
        elif sel == '4':
            self.view_all_opponents()
        elif sel == '5':
            self.add_new_opponent()
        elif sel == '6':
            self.delete_existing_opponent()
        elif sel == '7':
            self.matches_by_opponent()
        elif sel == '8':
            self.matches_by_date()
        elif sel.lower() == 'exit':
            exit_program()
        else:
            show_user_error()
            self.options()

    def view_all_matches(self):
        print_header('ALL MATCHES:')
        all_matches = [value for key, value in Match.all.items()]
        if all_matches:
            for match in all_matches:
                spacing = calc_match_spacing(match)
                print(f'ID: {match.id}{spacing}| DATE: {match.date} | OUTCOME: {"W" if match.outcome == 1 else "L"} | OPPONENT: {match.opponent_id}')
                print('------')
        else:
            print('No existing match records.')
        self.options()

    def add_new_match(self):
        print_header('ADD NEW MATCH:')
        print('In order to add a new match, you must know the opponent ID.')
        choice = check_proceed()
        if choice == '1':
            try:
                date = input('Enter date (MM-DD-YY): ')
                outcome = input('Enter outcome (1 = win, 0 = loss): ')
                opponent_id = input('Enter opponent ID: ')
                Match.create_match(date=date, outcome=outcome, opponent_id=opponent_id)
                print('Successfully added new match!')
                self.options()
            except Exception as e:
                show_user_error(e)
                self.add_new_match()
        elif choice == '2':
            clear_screen()
            self.options()
        else:
            show_user_error()
            self.add_new_match()

    def delete_existing_match(self):
        print_header('DELETE MATCH:')
        print('In order to delete a match, you must know the match ID.')
        choice = check_proceed()
        if choice == '1':
            try:
                match_id = int(input('Enter match ID: '))
                match = Match.find_by_id(match_id)
                match.delete_match()
                print('Successfully deleted match!')
                self.options()
            except:
                show_user_error('Invalid match ID. Please try again.')
                self.delete_existing_match()
        elif choice == '2':
            clear_screen()
            self.options()
        else:
            show_user_error()
            self.delete_existing_match()

    def view_all_opponents(self):
        print_header('ALL OPPONENTS:')
        all_opponents = [value for key, value in Opponent.all.items()]
        if all_opponents:
            for opponent in all_opponents:
                spacing = calc_match_spacing(opponent)
                print(f'ID: {opponent.id}{spacing}| {opponent.name}')
                print('------')
        else:
            print('No existing opponent records.')
        self.options()

    def add_new_opponent(self):
        print_header('ADD NEW OPPONENT:')
        print('In order to add a new opponent, you must enter the opponent\'s name.')
        choice = check_proceed()
        if choice == '1':
            name = input('Enter name: ')
            try:
                Opponent.create_opponent(name=name)
                print('Successfully added new opponent!')
                self.options()
            except Exception as e:
                show_user_error(e)
                self.add_new_opponent()
        elif choice == '2':
            clear_screen()
            self.options()
        else:
            show_user_error()
            self.add_new_opponent()

    def delete_existing_opponent(self):
        print_header('DELETE OPPONENT:')
        print('In order to delete an opponent, you must know the opponent ID.')
        choice = check_proceed()
        if choice == '1':
            try:
                opponent_id = int(input('Enter opponent ID: '))
                opponent = Opponent.find_by_id(opponent_id)
                opponent.delete_opponent()
                print('Successfully deleted opponent!')
                self.options()
            except:
                show_user_error('Invalid opponent ID. Please try again.')
                self.delete_existing_opponent()
        elif choice == '2':
            clear_screen()
            self.options()
        else:
            show_user_error()
            self.delete_existing_opponent()

    def matches_by_opponent(self):
        print_header('SEARCH MATCHES BY OPPONENT:')
        print('In order to search matches by opponent, you must know the opponent ID.')
        choice = check_proceed()
        if choice == '1':
            try:
                opponent_id = int(input('Enter opponent ID: '))
                opponent = Opponent.find_by_id(opponent_id)
                matches = opponent.get_matches()
                clear_screen()
                print(f'MATCHES AGAINST {opponent.name.upper()}:')
                print('')
                for match in matches:
                    spacing = calc_match_spacing(match)
                    print(f'ID: {match.id}{spacing}| DATE: {match.date} | OUTCOME: {"W" if match.outcome == 1 else "L"} | OPPONENT: {match.opponent_id}')
                    print('------')
                self.options()
            except:
                show_user_error('Invalid opponent ID. Please try again.')
                self.matches_by_opponent()
        elif choice == '2':
            clear_screen()
            self.options()
        else:
            show_user_error()
            self.matches_by_opponent()

    def matches_by_date(self):
        print_header('SEARCH MATCHES BY DATE:')
        print('In order to search matches by date, you must enter a start date and end date.')
        choice = check_proceed()
        if choice == '1':
            try:
                start = input('Enter start date (MM-DD-YY): ')
                end = input('Enter end date (MM-DD-YY): ')
                matches = Match.search_by_date(start, end)
                clear_screen()
                print(f'MATCHES FROM {start} TO {end}:')
                print('')
                for match in matches:
                    spacing = calc_match_spacing(match)
                    print(f'ID: {match.id}{spacing}| DATE: {match.date} | OUTCOME: {"W" if match.outcome == 1 else "L"} | OPPONENT: {match.opponent_id}')
                    print('------')
                self.options()
            except:
                show_user_error('Invalid dates. Please try again.')
                self.matches_by_opponent()
        elif choice == '2':
            clear_screen()
            self.options()
        else:
            show_user_error()
            self.matches_by_date()