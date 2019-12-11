# Author: Chase Karlen
# Email: chase@uky.edu
# Section: 002
# Received help from: Ashton Kheradmand (Section 003) - Ashton.Kheradmand@uky.edu
# Used several code excerpts from Ashton
"""
Purpose: To get choice user inputs
Pre: No parameters
Post: User input validated string

print menu

while loop for input validation
    ask user for input
return input
"""
def get_choice():
    print("\nMain Menu\n\n1. Load database\n2. Save database\n"
          "3. Enter new record\n4. Delete existing record\n"
          "5. Search database\n6. Sort by key (ID) field\n7. Display database\nQ. Quit\n")
    choice = input("> ")

    while choice != "1" and choice != "2" and choice != "3" and \
            choice != "4" and choice != "5" and choice != "6" and \
            choice != "7" and choice != "Q" and choice != "q":
        print("Invalid choice")
        choice = input("> ")

    return choice


"""
Purpose: To display database
Pre: One parameter (database list)
Post: Displays the database list in columnar format

for contents in database list:
    print contents
"""
def display(db):
    print("------------------------------------------------------")
    print("ID\tEmployee name\tDepartment\tSupervisor\n")

    for i in range(len(db)):
        print(db[i][0], '\t', db[i][1] + "" + db[i][2], '\t', db[i][3], '\t', db[i][4])

    print("------------------------------------------------------")


"""
Purpose: To load database from file
Pre: No parameters
Post: Database list loaded from file

initialize database_list
ask user for filename
define flag to False
while not flag:
    try:
        open file
        set flag to True
        print file is open
        for contents in open file:
            append [contents] to database_list
        return database_list
    except IOError:
        print file won't open
        ask user for filename
"""
def load():
    database_list = []
    file_name = input("filename? ")
    ok = False
    while not ok:
        try:
            contents = open(file_name + ".txt", "r")
            ok = True
            print(file_name, "loaded")

            for file in contents:
                file = file.strip().split(",")
                database_list.append(file)

            return database_list

        except IOError:
            print("Error, file would not open")
            file_name = input("filename? ")


"""
Purpose: To sort the database (ascending or descending)
Pre: One parameter (database list)
Post: Modified list after sort (not printed)

ask user for ascending or descending

if ascending:
    for contents in database list:
        sort database list
else:
    for contents in database list:
        sort database list reverse=True

return database list
"""
def sort_list(db):
    user_input = input("Ascending or Descending? (a/d) ")
    if user_input == "a":
        db.sort()
        print("list sorted")
    else:
        db.sort(reverse=True)
        print("list sorted")


"""
Purpose: To save the database
Pre: One parameter (database list)
Post: No return value (file is simply saved)

ask user for filename to save data to

open user filename to write
write database list to user filename
close file
"""
def save(db):
    user_input = input("Filename: ")
    file = open(user_input + ".txt", "w")

    for i in range(len(db)):
        for j in range(len(db[i])):
            file.write(str(db[i][j]) + ",")
        file.write("\n")

    file.close()
    print(user_input, "saved!")


"""
Purpose: To add a new record to database list
Pre: One parameter (database list)
Post: No return value (database is changed)

ask user for ID number

if ID is in list:
    print ID is already in list
else:
    ask user for first name, last name, department, supervisor
    append new variables to database list
"""
def newrecord(db):
    user_input = input("ID number: ")
    does_exist = False

    for i in range(len(db)):
        for j in range(len(db[i])):
            if db[i][j] == user_input:
                print("ID already exists!")
                does_exist = True

    if not does_exist:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        department = input("Department: ")
        supervisor = input("Supervisor: ")
        db.append([user_input, first_name, last_name, department, supervisor])
        print(user_input, "added!")


"""
Purpose: To remove a record from database list
Pre: One parameter (database list)
Post: No return value (database is not changed/changed)

ask user for ID to remove
if ID exists:
    for loop to index list:
    remove index where ID is
else:
    print ID not found
"""
def remove_record(db):
    user_input = input("ID number: ")
    does_exist = False

    for i, db_list in enumerate(db):
        for j, elem in enumerate(db_list):
            if elem == user_input:
                does_exist = True
                db.pop(i)
                print(user_input, "removed!")

    if not does_exist:
        print("ID not found!")


"""
Purpose: To search for a particular field in database list
Pre: One parameter (database list)
Post: Result of search

ask user if wanting to search for ID, first name, last name, department,
supervisor

while user input is not ID, first name, last name, department,
supervisor:
    print invalid choice
    ask for input again

ask user string to search for based on above input
call search with string to search, database list, and column
if list is not empty:
    prompt to save
    if prompt is yes:
        call save
"""
def search_menu(db):
    print("Search menu\n\n0. Key (ID)\n1. First name\n2. Last name\n3. Department\n"
          "4. Supervisor\n")

    user_input = input("> ")

    while user_input != "0" and user_input != "1" and user_input != "2" and \
            user_input != "3" and user_input != "4":
        print("Invalid choice!")
        user_input = input("> ")

    if user_input == "0":
        id_search = input("String to search for? ")
        get_search = search(id_search, db, 0)
        display(get_search)
        if get_search:
            user_input = input("Do you want to save this as a separate file? (y/n): ")
            if user_input == "y":
                save(get_search)
    elif user_input == "1":
        f_name = input("String to search for? ")
        get_search = search(f_name, db, 1)
        display(get_search)
        if get_search:
            user_input = input("Do you want to save this as a separate file? (y/n): ")
            if user_input == "y":
                save(get_search)
    elif user_input == "2":
        l_name = input("String to search for? ")
        get_search = search(l_name, db, 2)
        display(get_search)
        if get_search:
            user_input = input("Do you want to save this as a separate file? (y/n): ")
            if user_input == "y":
                save(get_search)
    elif user_input == "3":
        department = input("String to search for? ")
        get_search = search(department, db, 3)
        display(get_search)
        if get_search:
            user_input = input("Do you want to save this as a separate file? (y/n): ")
            if user_input == "y":
                save(get_search)
    else:
        supervisor = input("String to search for? ")
        get_search = search(supervisor, db, 4)
        display(get_search)
        if get_search:
            user_input = input("Do you want to save this as a separate file? (y/n): ")
            if user_input == "y":
                save(get_search)


"""
Purpose: To search for anything in database list
Pre: Three parameters (string to search (string), database list (db), column to search in (col))
Post: Returns a new list that contains records that match string to search,
      Returns nothing if nothing is found matches string

initialize empty list
for i in range of len of database list:
    if database list[i][col] equals string:
        append database list[i] to empty list
        
return list
"""
# Received help from Ashton here
def search(string, db, col):
    found_list = []

    for i in range(len(db)):
        if db[i][col] == string:
            found_list.append(db[i])

    return found_list


"""
Purpose: To run program
Pre: No parameters
Post: Returns based on user input

call get_choice to get user input and validation
if get_choice() is 1, 2, 3, 4, 5, 6, 7, Q, q:
    call to perspective functions based off input
"""
def main():
    is_saved = False
    database_list = []
    print("Employee Database")

    choice = get_choice()

    while choice != "Q" and choice != "q":
        if choice == "1":
            database_list = load()
            is_saved = True
        elif choice == "2":
            save(database_list)
            is_saved = True
        elif choice == "3":
            newrecord(database_list)
            is_saved = False
        elif choice == "4":
            remove_record(database_list)
            is_saved = False
        elif choice == "5":
            search_menu(database_list)
        elif choice == "6":
            sort_list(database_list)
            is_saved = False
        else:
            display(database_list)

        choice = get_choice()

    if not is_saved:
        user_input = input("File is not saved.  Save? (y/n): ")
        if user_input == "y":
            save(database_list)
        else:
            print("File not saved! Quitting anyway...")


main()


# ---------------------------------------------------------------------------
# To use this:  comment out the call to main and put this code (all of it)
#  at the bottom of your .py file.
#  choose which test or tests are run by setting that boolean to True
#   just uncomment it and comment out the line setting it to False
# NOTE: your function names MUST match what the assignment gives!
# ---------------------------------------------------------------------------


test_display = False

test_sort_list = False

test_load = False

test_save = False

test_search_menu = False

test_search = False

test_newrecord = False

test_remove_record = False

if test_display:
    print("Display test\n")
    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['1112', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['1113', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1120', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("testing display, with 4 employees")
    display(dblist)
    print()

    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("testing display, with 1 employee")
    display(dblist)
    print()

    dblist = []
    print("testing display, with 0 employees")
    display(dblist)
    print()

if test_sort_list:
    print("***********************************************sort_list")
    dblist = []
    print("Sorting with 0 employees\n")
    print("Give Ascending as input")
    print("Before sort", dblist)
    sort_list(dblist)
    print("After sort", dblist)

    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("\nSorting with one employee\n")
    print("Give Ascending as input")
    print("Before sort", dblist)
    sort_list(dblist)
    print("After sort", dblist)

    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("\nSorting with one employee\n")
    print("Give Descending as input")
    print("Before sort", dblist)
    sort_list(dblist)
    print("After sort", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]

    print("\nSorting with 4 employees\n")
    print("Give Descending as input")
    print("Before sort", dblist)
    sort_list(dblist)
    print("After sort", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]

    print("\nSorting with 4 employees\n")
    print("Give Ascending as input")
    print("Before sort", dblist)
    sort_list(dblist)
    print("After sort", dblist)

if test_load:
    print("***********************************************load")
    print("\nGive filename that exists")
    table = load()
    print("After load, table is", table)

    print("\nGive filename that does not exist, then one that exists")
    table = load()
    print("After load, table is", table)

    print("\nGive filename that exists but is empty")
    table = load()
    print("After load, table should be empty, table is", table)

if test_save:
    lst = []
    print("***********************************************save")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Saving with 4 employees")
    print("Before save, list is", dblist)
    save(dblist)
    print("After save, list is", dblist)
    print("Check your output file, should have 4 lines")

    dblist = []
    print("Saving with 0 employees")
    print("Before save, list is empty", dblist)
    save(dblist)
    print("After save, list is", dblist)
    print("Check your output file, should be empty")

    dblist = [['1111', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("Saving with 1 employee")
    print("Before save, list is", dblist)
    save(dblist)
    print("After save, list is", dblist)
    print("Check your output file, should have 1 line")

if test_search_menu:
    print("***********************************************search_menu")
    print("Choose 0 and 2222 and N")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for 2222 as ID", result)
    print("result should be ['2222','John','Smith','Purchasing','Ron Sloan']\n")

    print("Choose 0 and 5555")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for 5555 as ID", result)
    print("result should be []\n")

    print("Choose 1 and Mary and n")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Mary as First Name", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen']]\n")

    print("Choose 1 and Sue")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Sue as First Name", result)
    print("result should be []\n")

    print("Choose 2 and Brown and N")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Brown as Last Name", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'] ]\n")

    print("Choose 2 and Black")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Black as Last Name", result)
    print("result should be []\n")

    print("Choose 3 and Purchasing and Y and a filename")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Purchasing as Department", result)
    print("result should be [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],"
          "['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan']]\n")

    print("Choose 3 and Administration")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Administration as Department", result)
    print("result should be []\n")

    print("Choose 4 and Bob Wallen and y and a filename")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Bob Wallen as Supervisor", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen']] \n")

    print("Choose 4 and Brian Kramer")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Brian Kramer as Supervisor", result)
    print("result should be []\n")

    print("Choose 9 and 4 and Ron Sloan and n")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search_menu(dblist)
    print("Result of search for Ron Sloan as Supervisor", result)
    print("result should be [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],"
          "['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan']]\n")

if test_search:
    print("***********************************************search")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Searching for 4444 as ID")
    result = search("4444", dblist, 0)
    print("result is", result)
    print("result should be ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan']\n")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Searching for 6666 as ID")
    result = search("6666", dblist, 0)
    print("result is", result)
    print("result should be []\n")

    dblist = []
    print("Searching for 6666 as ID in empty list")
    result = search("6666", dblist, 0)
    print("result is", result)
    print("result should be []\n")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search("Bob Wallen", dblist, 4)
    print("Result of search for Bob Wallen as Supervisor", result)
    print("result should be [['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen']] \n")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    result = search("Brian Kramer", dblist, 4)
    print("Result of search for Brian Kramer as Supervisor", result)
    print("result should be []\n")

    dblist = []
    result = search("Bob Wallen", dblist, 4)
    print("Result of search for Bob Wallen as Supervisor in an empty list", result)
    print("result should be []\n")

if test_newrecord:
    lst = []
    print("***********************************************newrecord")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Enter 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(dblist)
    print("After new record added", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Enter 4444 then 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(dblist)
    print("After new record added", dblist)

    dblist = []
    print("Adding to an empty list")
    print("Enter 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(dblist)
    print("After new record added", dblist)

    print("Adding to a list with 1 employee")
    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("Enter 5555, Ron, Thomas, Warehouse1, Sam Landen")
    print("Before new record added", dblist)
    newrecord(dblist)
    print("After new record added", dblist)

if test_remove_record:
    print("***********************************************remove_record")

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Enter 1111")
    print("Before record removed", dblist)
    remove_record(dblist)
    print("After record removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Removing a record at the end of the list")
    print("Enter 1111")
    print("Before record removed", dblist)
    remove_record(dblist)
    print("After record removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Removing a record not in list")
    print("Enter 5555")
    print("Before record removed", dblist)
    remove_record(dblist)
    print("After record not removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan'],
              ['4444', 'Sam', 'Thomas', 'Purchasing', 'Ron Sloan'],
              ['3333', 'Mary', 'Brown', 'Accounting', 'Bob Wallen'],
              ['1111', 'David', 'Drake', 'Warehouse1', 'Sam Landen']]
    print("Removing a record at the front of the list")
    print("Enter 2222")
    print("Before record removed", dblist)
    remove_record(dblist)
    print("After record removed", dblist)

    dblist = [['2222', 'John', 'Smith', 'Purchasing', 'Ron Sloan']]
    print("Removing a record from list with 1 employee")
    print("Enter 2222")
    print("Before record removed", dblist)
    remove_record(dblist)
    print("After record removed", dblist)
