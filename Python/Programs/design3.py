"""
get_choice

Purpose: To get choice user inputs
Pre: No parameters
Post: User input validated string

print menu

while loop for input validation
    ask user for input
return input
------------------------------------------------

display

Purpose: To display database
Pre: One parameter (database list)
Post: Displays the database list in columnar format

for contents in database list:
    print contents
------------------------------------------------

sort_list

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
------------------------------------------------

load

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
------------------------------------------------

save

Purpose: To save the database
Pre: One parameter (database list)
Post: No return value (file is simply saved)

ask user for filename to save data to

open user filename to write
write database list to user filename
close file
------------------------------------------------

newrecord

Purpose: To add a new record to database list
Pre: One parameter (database list)
Post: No return value (database is changed)

ask user for ID number

if ID is in list:
    print ID is already in list
else:
    ask user for first name, last name, department, supervisor
    append new variables to database list
------------------------------------------------

remove_record

Purpose: To remove a record from database list
Pre: One parameter (database list)
Post: No return value (database is not changed/changed)

ask user for ID to remove
if ID exists:
    for loop to index list:
    remove index where ID is
else:
    print ID not found
------------------------------------------------

search_menu

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

------------------------------------------------

search

Purpose: To search for anything in database list
Pre: Three parameters (string to search, database list, column to search in)
Post: Returns a new list that contains records that match string to search,
      Returns nothing if nothing is found matches string


------------------------------------------------

main

Purpose: To run program
Pre: No parameters
Post: Returns based on user input

call get_choice to get user input and validation
if get_choice() is 1, 2, 3, 4, 5, 6, 7, Q, q:
    call to perspective functions based off input
"""

