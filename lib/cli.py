from helpers import (
    clear_screen,
    print_header,
    show_user_error,
    check_return_to_main_menu,
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
            show_user_error(e='Invalid selection. Please try again.')
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
        check_return_to_main_menu(self, id)
        try:
            match = Match.find_by_id(int(id))
            clear_screen()
            print('')
            print_match(match)
        except:
            show_user_error(e='Invalid match ID. Please try again.')
            self.find_match_by_id()
        self.options()

    def add_new_match(self):
        print_header('ADD NEW MATCH:')
        date = input('Enter date in MM-DD-YY format (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, date)
        
        outcome = input('Enter outcome (1 = win, 0 = loss): ')
        opponent_id = input('Enter opponent ID: ')
        try:
            match = Match.create_match(date=date, outcome=outcome, opponent_id=opponent_id)
            match.save()
            print('Successfully added new match!')
        except Exception as e:
            show_user_error(e)
            self.add_new_match()
        self.options()

    def update_match(self):
        print_header('UPDATE MATCH:')
        id = input('Enter match id (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, id)

        try:
            match = Match.find_by_id(int(id))
            print('')
            print('Match to be updated:')
            print_match(match)
        except:
            show_user_error(e='Invalid match ID. Please try again.')
            self.update_match()
        
        try:
            date = input('Enter new date in MM-DD-YY format: ')
            outcome = input('Enter new outcome (1 = win, 0 = loss): ')
            opponent_id = input('Enter new opponent ID: ')
            updated_match = Match(date=date, outcome=outcome, opponent_id=opponent_id, id=int(id))
            updated_match.update_match()
            print('Successfully updated match!')
        except Exception as e:
            show_user_error(e)
            self.update_match()
        self.options()

    def delete_match(self):
        print_header('DELETE MATCH:')
        match_id = input('Enter match ID (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, match_id)
        try:
            match_id_int = int(match_id)
            match = Match.find_by_id(match_id_int)
            match.delete_match()
            print('Successfully deleted match!')
        except:
            show_user_error(e='Invalid match ID. Please try again.')
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
        check_return_to_main_menu(self, id)
        try:
            opponent = Opponent.find_by_id(int(id))
            clear_screen()
            print('')
            print_opponent(opponent)
        except:
            show_user_error(e='Invalid opponent ID. Please try again.')
            self.find_opponent_by_id()
        self.options()

    def add_new_opponent(self):
        print_header('ADD NEW OPPONENT:')
        name = input('Enter name (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, name)
        try:
            opponent = Opponent.create_opponent(name=name)
            opponent.save()
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
        opp_id = input('Enter opponent ID (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, opp_id)
        try:
            opp_id_int = int(opp_id)
            opponent = Opponent.find_by_id(opp_id_int)
            opponent.delete_opponent()
            print('Successfully deleted opponent!')
        except:
            show_user_error(e='Invalid opponent ID. Please try again.')
            self.delete_opponent()
        self.options()

    def matches_by_opponent(self):
        print_header('SEARCH MATCHES BY OPPONENT:')
        opp_id = input('Enter opponent ID (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, opp_id)
        try:
            opp_id_int = int(opp_id)
            opponent = Opponent.find_by_id(opp_id_int)
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
            show_user_error(e='Invalid opponent ID. Please try again.')
            self.matches_by_opponent()
        self.options()

    def matches_by_date(self):
        print_header('SEARCH MATCHES BY DATE:')
        start = input('Enter start date in MM-DD-YY format (or type "m" to return to main menu): ')
        check_return_to_main_menu(self, start)
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
            show_user_error(e='Invalid dates. Please try again.')
            self.matches_by_date()
        self.options()