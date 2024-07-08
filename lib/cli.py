from helpers import (
    clear_screen,
    print_header,
    show_user_error,
    check_proceed,
    return_to_main_menu,
    print_match,
    print_opponent,
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
        print('-- Query Matches --')
        print('Type "1" to view all matches')
        print('Type "2" to find match by ID')
        print('Type "3" to add new match')
        print('Type "4" to update match')
        print('Type "5" to delete match')
        print('')
        print('-- Query Opponents --')
        print('Type "6" to view all opponents')
        print('Type "7" to find opponent by ID')
        print('Type "8" to add new opponent')
        print('Type "9" to update opponent')
        print('Type "10" to delete opponent')
        print('')
        print('-- Filter Matches --')
        print('Type "11" to search matches by opponent')
        print('Type "12" to search matches by date')
        print('')
        print('Type "exit" to exit program')
        print('')
        self.selection()

    def selection(self):
        sel = input('Enter selection: ')
        clear_screen()
        if sel == '1':
            self.view_all_matches()
        elif sel == '2':
            self.find_match_by_id()
        elif sel == '3':
            self.add_new_match()
        elif sel == '4':
            self.update_match()
        elif sel == '5':
            self.delete_match()
        elif sel == '6':
            self.view_all_opponents()
        elif sel == '7':
            self.find_opponent_by_id()
        elif sel == '8':
            self.add_new_opponent()
        elif sel == '9':
            self.update_opponent()
        elif sel == '10':
            self.delete_opponent()
        elif sel == '11':
            self.matches_by_opponent()
        elif sel == '12':
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
                print_match(match)
        else:
            print('No existing match records.')
        self.options()

    def find_match_by_id(self):
        print_header('FIND MATCH BY ID:')
        id = input('Enter match id (or type "m" to return to main menu): ')
        if id == 'm' or id == 'M':
            return_to_main_menu(self)
        else:
            try:
                match = Match.find_by_id(int(id))
                clear_screen()
                print('')
                print_match(match)
            except:
                show_user_error('Invalid match ID. Please try again.')
                self.find_match_by_id()
        self.options()

    def add_new_match(self):
        print_header('ADD NEW MATCH:')
        date = input('Enter date in MM-DD-YY format (or type "m" to return to main menu): ')
        if date == 'm' or date == 'M':
            return_to_main_menu(self)
        else:
            outcome = input('Enter outcome (1 = win, 0 = loss): ')
            opponent_id = input('Enter opponent ID: ')
            
            # Account for non-integer opponent_id input
            try:
                opponent_id = int(opponent_id)
            except:
                show_user_error('Opponent ID must be an integer. Please try again.')
                self.add_new_match()
            
            # Check if integer opponent_id exists and create the match - catch any subsequent errors in date or outcome
            try:
                opponent = Opponent.all.get(opponent_id)
                if opponent:
                    Match.create_match(date=date, outcome=outcome, opponent_id=opponent_id)
                    print('Successfully added new match!')
                else:
                    show_user_error('Invalid opponent ID. Please try again.')
                    self.add_new_match()
            except Exception as e:
                show_user_error(e)
                self.add_new_match()
        self.options()

    def update_match(self):
        pass

    def delete_match(self):
        print_header('DELETE MATCH:')
        match_id = input('Enter match ID (or type "m" to return to main menu): ')
        if match_id == 'm' or match_id == 'M':
            return_to_main_menu(self)
        else:
            try:
                match_id_int = int(match_id)
                match = Match.find_by_id(match_id_int)
                match.delete_match()
                print('Successfully deleted match!')
            except:
                show_user_error('Invalid match ID. Please try again.')
                self.delete_match()
        self.options()

    def view_all_opponents(self):
        print_header('ALL OPPONENTS:')
        all_opponents = [value for key, value in Opponent.all.items()]
        if all_opponents:
            for opponent in all_opponents:
                print_opponent(opponent)
        else:
            print('No existing opponent records.')
        self.options()

    def find_opponent_by_id(self):
        print_header('FIND OPPONENT BY ID:')
        id = input('Enter opponent id (or type "m" to return to main menu): ')
        if id == 'm' or id == 'M':
            return_to_main_menu(self)
        else:
            try:
                opponent = Opponent.find_by_id(int(id))
                clear_screen()
                print('')
                print_opponent(opponent)
            except:
                show_user_error('Invalid match ID. Please try again.')
                self.find_opponent_by_id()
        self.options()

    def add_new_opponent(self):
        print_header('ADD NEW OPPONENT:')
        name = input('Enter name (or type "m" to return to main menu): ')
        if name == 'm' or name == 'M':
            return_to_main_menu(self)
        else:
            try:
                Opponent.create_opponent(name=name)
                print('Successfully added new opponent!')
            except Exception as e:
                show_user_error(e)
                self.add_new_opponent()
        self.options()

    def update_opponent(self):
        pass

    def delete_opponent(self):
        print_header('DELETE OPPONENT:')
        print('**IMPORTANT NOTE: Deleting an opponent will also delete any associated match records.**')
        print('')
        print('Opponent ID is required.')
        choice = check_proceed()
        if choice == '1':
            try:
                opponent_id = int(input('Enter opponent ID: '))
                opponent = Opponent.find_by_id(opponent_id)
                opponent.delete_opponent()
                print('Successfully deleted opponent!')
            except:
                show_user_error('Invalid opponent ID. Please try again.')
                self.delete_opponent()
        elif choice == '2':
            return_to_main_menu(self)
        else:
            show_user_error()
            self.delete_opponent()
        self.options()

    def matches_by_opponent(self):
        print_header('SEARCH MATCHES BY OPPONENT:')
        print('Opponent ID is required.')
        choice = check_proceed()
        if choice == '1':
            try:
                opponent_id = int(input('Enter opponent ID: '))
                opponent = Opponent.find_by_id(opponent_id)
                matches = opponent.get_matches()
                clear_screen()
                print(f'MATCHES AGAINST {opponent.name.upper()}:')
                print('')
                if matches:
                    for match in matches:
                        print_match(match)
                else:
                    print('No match records against this opponent.')
            except:
                show_user_error('Invalid opponent ID. Please try again.')
                self.matches_by_opponent()
        elif choice == '2':
            return_to_main_menu(self)
        else:
            show_user_error()
            self.matches_by_opponent()
        self.options()

    def matches_by_date(self):
        print_header('SEARCH MATCHES BY DATE:')
        print('Start and end dates are required.')
        choice = check_proceed()
        if choice == '1':
            start = input('Enter start date (MM-DD-YY): ')
            end = input('Enter end date (MM-DD-YY): ')
            try:
                matches = Match.search_by_date(start, end)
                clear_screen()
                print(f'MATCHES FROM {start} TO {end}:')
                print('')
                if matches:
                    for match in matches:
                        print_match(match)
                else:
                    print('No match records during this date range.')
            except:
                show_user_error('Invalid dates. Please try again.')
                self.matches_by_date()
        elif choice == '2':
            return_to_main_menu(self)
        else:
            show_user_error()
            self.matches_by_date()
        self.options()