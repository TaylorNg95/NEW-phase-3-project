# Match Log Tracker

This Python Command Line Interface (CLI) application serves as a match log for sports teams and/or individual competitors. The program utilizes SQLite3 and object-relational mapping (ORM) methods to manage opponent and match models. Users must create at least one new opponent record in order to create a new match record. The program has full CRUD capabilities, allowing for users to view, add, delete, and update both opponent data and match data. Users may log a match record by providing the following details: match date (mm-dd-yy), match outcome (1 = win, 0 = loss), and opponent ID (unique identifier created for each new opponent record).

## Requirements

This application requires Python version 3.8.13.

## Installation and Usage (how to install and use your app)

From the root project directory, type 'pipenv install' to create your virtual environment and install the necessary dependencies. Type 'pipenv shell' to activate the virtual environment. To run this application, change directory into the 'lib' folder. Within this foolder, you will find the following: run.py, helpers.py, cli.py, and models folder (contains __init__.py and match and opponent models). Once in the ./lib directory, type './run.py' to start the program. This will initiate the command line interface, which runs from the 'cli.py' file. You should see a welcome message that says 'WELCOME TO YOUR MATCH LOG!' along with a menu of options from which you can select. You will always be redirected back to this menu after making a selection(s) and following the necessary instruction(s). Exit the program at any time by typing 'exit' from the main menu.

### Option: Query Matches

Users may type any of the options from the main menu numbered 1-5 in order to make queries related to matches logged in their tracker. These include: (1) viewing all match records, (2) finding a match by ID, (3) adding a new match, (4) updating a match, and (5) deleting a match. Based on user selection, a unique Cli method will be run, which calls the necessary ORM method(s) of the applicable model class(es) to perform the required operation. Users may be prompted for additional input as required.

1. [TBD - option 1]
2. [TBD - option 2]
3. [TBD - option 3]
4. [TBD - option 4]
5. [TBD - option 5] 

### Option: Query Opponents

Users may type any of the options from the main menu numbered 6-10 in order to make queries related to opponents logged in their tracker. These include: (1) viewing all opponent records, (2) finding an opponent by ID, (3) adding a new opponent, (4) updating an opponent, and (5) deleting an opponent. Based on user selection, a unique Cli method will be run, which calls the necessary ORM method(s) of the applicable model class(es) to perform the required operation. Users may be prompted for additional input as required.

6. [TBD - option 6]
7. [TBD - option 7]
8. [TBD - option 8]
9. [TBD - option 9]
10. [TBD - option 10]

### Option: Filter Matches

Users may type either 11 or 12 in order to filter the matches logged in their tracker based on opponent or based on date range. For either option, a unique Cli method will be run, which calls the necessary ORM method(s) of the applicable model class(es) to perform the required operation. Users will be prompted for additional input related to either their desired or opponent or desired date range.

11. [TBD - option 11]
12. [TBD - option 12]

## License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.