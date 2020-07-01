import cs50
from sys import exit, argv


class Roster:
    def main(self):

        # Getting house name
        house_name = argv[-1]
        # Selecting the database
        db = cs50.SQL("sqlite:///students.db")

        # List to check if last name is same for any students
        last_name_list = []
        # Getting last names from table
        last_names_dict = db.execute(f"SELECT last FROM students")
        # Storing last names in a list
        for row in last_names_dict:
            last_name_list.append(row['last'])

        # Checking for duplicate last names
        if len(set(last_name_list)) == len(last_name_list):
            # Returns a dictionary of students ordered by first name
            student = db.execute(
                f"SELECT first, middle, last, birth FROM students WHERE house = '{house_name}' ORDER BY first")
        else:
            student = db.execute(
                f"SELECT first, middle, last, birth FROM students WHERE house = '{house_name}' ORDER BY last")

        for row in student:
            if row['middle'] == "":
                print(row['first'], row['last'], sep=" ", end=", ")
                print(row['birth'])
            else:
                print(row['first'], row['middle'], row['last'], sep=" ", end=", ")
                print(row['birth'])

                
if __name__ == '__main__':
    Roster().main()
    if len(argv) != 2:
        print("Invalid command")
        exit(1)
