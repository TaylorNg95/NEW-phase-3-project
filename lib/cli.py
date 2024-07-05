from helpers import exit_program, clear_screen

class Cli:

    def run(self):
        clear_screen()
        print('WELCOME TO YOUR MATCH LOG!')
        print('')
        self.options()

    def options(self):
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
            print('Invalid input. Please try again!')
            print('')
            self.options()

    def view_all_matches(self):
        pass

    def add_new_match(self):
        pass

    def delete_existing_match(self):
        pass

    def view_all_opponents(self):
        pass

    def add_new_opponent(self):
        pass

    def delete_existing_opponent(self):
        pass

    def matches_by_opponent(self):
        pass

    def matches_by_date(self):
        pass