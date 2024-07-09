# MatchTracker

This Python Command Line Interface (CLI) application allows sports teams and/or individual competitors to track and manage their matches. The program utilizes SQLite3 and object-relational mapping (ORM) methods to manage opponent and match models. The program has full CRUD capabilities, allowing for users to view, add, delete, and update opponent data and match data. Match records consist of the following details: ID (unique identifier), match date (MM-DD-YY), match outcome (1 = win, 0 = loss), and opponent ID (unique identifier created for each new opponent record).

## Requirements

This application requires Python version 3.8.13.

## Installation and Usage

From the root project directory, type 'pipenv install' and 'pipenv shell' to activate your virtual environment and install the necessary dependencies. To run this application, change directory into the 'lib' folder. Within this folder, you will see the following: run.py, helpers.py, cli.py, and models folder (contains __init__.py and match and opponent models). From the lib directory, type './run.py' to start the program. This will initiate the command line interface, which runs from the 'cli.py' file. You should see a welcome message that says 'WELCOME TO YOUR MATCH LOG!' along with an options menu from which you can select any of 12 options. You will always be redirected back to this menu after making a selection and following the necessary instruction(s). Exit the program at any time by typing 'exit' from the options menu.

### Options 1-5: Query Matches

Users may type any of the options from the options menu numbered 1-5 in order to make queries related to their tracked. These include: (1) view all match records, (2) find a match by ID, (3) add a new match, (4) update a match, and (5) delete a match. Based on user selection, a unique Cli method will be run, which calls the necessary ORM method(s) of the applicable model class(es) to perform the required operation. Users may be prompted for additional input as required.

1. **View all matches**: prints all existing match records and related opponent name (attributes: ID, date, outcome, opponent name).
2. **Find match by ID**: prompts user for match ID and prints the corresponding record.
3. **Add new match**: prompts user for date, outcome, and opponent ID to create new match record. Opponent ID is required, as match have an associated opponent, and program verifies opponent ID exists prior to creating new record. Note that users must create at least one new opponent record first (see option 8) in order to create a new match record.
4. **Update match**: prompts user for match ID associated with the record to be updated. Once verified, the program then prompts user for new date, new outcome, and new opponent ID to update the corresponding record.
5. **Delete match**: prompts user for match ID and deletes the associated record.

### Options 6-10: Query Opponents

Users may type any of the options from the options menu numbered 6-10 in order to make queries related to their tracked opponents. These include: (1) view all opponent records, (2) find an opponent by ID, (3) add a new opponent, (4) update an opponent, and (5) delete an opponent. Based on user selection, a unique Cli method will be run, which calls the necessary ORM method(s) of the applicable model class(es) to perform the required operation. Users may be prompted for additional input as required.

6. **View all opponents**: prints all existing opponent records (attributes: ID, name)
7. **Find opponent by ID**: prompts user for opponent ID and prints the corresponding record.
8. **Add new opponent**: prompts user for name to create new opponent record.
9. **Update opponent**: prompts user for opponent ID associated with the record to be updated. Once verified, the program then prompts user for new name to update the corresponding record.
10. **Delete opponent**: prompts user for opponent ID of the record to be deleted. Program alerts user that deleting an opponent also results in deletion of all associated match records, as a match must have an associated opponent. Once opponent ID is input, the program deletes all associated records.

### Options 11-12: Filter Matches

Users may type either 11 or 12 from the options menu in order to filter their tracked matches based on opponent or based on date range. For either option, a unique Cli method will be run, which calls the necessary ORM method(s) of the applicable model class(es) to perform the required operation. Users will be prompted for additional input related to either their desired opponent or desired date range.

11. **Matches by opponent**: prompts user for opponent ID and verifies that the ID exists before printing the corresponding match records. 
12. **Matches by date**: prompts user for date range and prints the corresponding match records.

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.