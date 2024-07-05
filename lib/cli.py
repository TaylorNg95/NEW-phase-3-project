from helpers import exit_program

class Cli:

    def run(self):
        print('WELCOME TO YOUR MATCH LOG!')
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
        self.selection()

    """ def main():
        while True:
            menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                helper_1()
            else:
                print("Invalid choice")


    def menu():
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Some useful function")


    if __name__ == "__main__":
        main() """