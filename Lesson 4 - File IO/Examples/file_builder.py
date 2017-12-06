import os

"""
STEP ONE: CREATE THE FILE AND WRITE ITS CONTENTS
"""

file_name = input("What is the name of your file?")

file_contents = input("Enter file contents...")

file_exists = os.path.isfile(file_name + ".txt")

# Before we create it, lets check to see if it already exists...
while(file_exists):

    # True

    answer = bool("The file name you have chosen already exists, would you like to overwrite it? (y or n)\n\r")

    if(answer == "y"):

        answer = True
    else:
        answer = False

    if(answer == True):

        create_file(file_name, file_contents)

    else:

        file_name = input("Pleass choose another name for your new file...")
        
if(file_exists == False):

    create_file(file_name, file_contents)
    
def create_file(file_name, file_contents):

    new_file = open(file_name + ".txt", "w")

    new_file.write(file_contents)

    new_file.close()

print("Your new file was successfully created!")

"""
STEP TWO: LOAD THE FILE AGAIN AND PRINT DATA TO CONFIRM CREATION
"""

file = open(file_name + ".txt", "r")

print("New file name: " + file.name)
print("New file contains: " + file.read())
file.close();
