import csv
from sys import argv, exit
import cs50


def store_data():
    """ Stores data is database """
    std_names = []
    std_house = []
    std_birth = []
    # Reading csv file
    filename = argv[-1]
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

        # for index, head in enumerate(header):
        #   print(index, head)

        for row in reader:
            std_names.append(row[0])
            std_house.append(row[1])
            std_birth.append(row[2])

    # Students_id
    std_id = 1
    # List carrying students name in a nested list
    std_det_names = []
    for name in std_names:
        std_det_names.append(name.split())

    # Selecting the database
    db = cs50.SQL("sqlite:///students.db")

    # To get house and birth year
    count = 0
    # Executes Loop the number of students
    for i in std_det_names:
        first_name = i[0]
        last_name = i[-1]
        house = std_house[count]
        birth_year = std_birth[count]
        count += 1

        # Sets middle name if it exists
        if len(i) == 3:
            middle_name = i[1]
        else:
            middle_name = ""

        # Writes to the Database file
        db.execute("INSERT INTO students (id, first, middle, last, house, birth) VALUES(?,?,?,?,?,?)",
                   std_id, first_name, middle_name, last_name, house, birth_year)

        # Incrementing student id
        std_id += 1

if __name__=='__main__':
    if len(argv) != 2:
        print("Invalid Command\nUsage: python import.py filename")
        exit(1)
    store_data()