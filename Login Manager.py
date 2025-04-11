# COMP 170 Standard Python Header
'''
Malachi Karczmar, Muhammad Javed
COMP170
Final Project
11APR25
'''
# Description:
'''
Program will have two possible function sequences:
    1 - create and store (encrypted) login credentials
            a. username generated with first name, last name, and date of birth
            b. password must:
                - contain an uppercase letter
                - contain a lowercase letter
                - contain a special character (any of the below):
                    !@$%^&*()_-+={[}]|\\:;"'<,>\\#.
                - contain a number
                - be atleast 8 characters in length
    2 - login using previously created login information (username and password pair)
'''
# Psuedo Code:
'''
0. Initialize Global Variables
    - N/A
    
1. def chooserBoi()
    - allow user to indicate function sequences
    
2. PASSWORD CREATOR:
    a. def display()
        - ask user how many accounts to create
    b. def userPass():
        - obtain a string from user
    c. def removeSpace():
        - remove spaces from any string passed to it
    d. def checkNumber()
        - check if string has at least one number
    e. def checkLength():
        - check length of string and ensure it is > 8
    f. def checkUpper():
        - check if string has atleast one uppercase character
    g. def checkLower():
        - check if string has atleast one lowercase character
    h. def checkSpecial():
        - check if string has atleast one special character (see description)
    i. def passCheck():
        - if inputted string satisfies all requirements, return True, else, return False
        
3. USERNAME CREATOR:
    a.
        -
    b.
        -
    c.
        -
    d.
        -

'''
# Program Code:

administratorPin = '0000'

def display():
    classSize = removeSpace(input("\nWelcome to your class's account creator!\nAll logins will be displayed after setup\n\
Please enter the class size (to skip additional account creation, press 0): "))
    while not classSize.isdigit():
        classSize = removeSpace(input("Please enter a number to indicate class size: "))
    return int(classSize)

def userPass(): # Get input from user and define password requirements
    userPass = str(input('''Please enter a password as described:\n- is at least 8 characters long\n- Contains at least one uppercase letter\n- Contains at least one lowercase letter\n- Contains at least one number\n- Contains at least one special character\nSpecial Characters are as follows\n ! @ $ % ^ & * ( ) - _ = + } ] { [ \\ | : ; " ' < . > / , \\# ?\n\n\nWARNING!: \nSpaces will not be accepted as input and will be removed.\n'''))
    return userPass

def removeSpace(passAttemptSpace): # Remove all spaces from user input
    passAttemptSpace = passAttemptSpace.replace(" ","")
    return passAttemptSpace

def checkNumber(userInput): # Verify  user input has a number in it
    hasNum = False
    for letter in userInput: # Use for-loop to analyze every character value and not whole string
        if letter.isdigit(): # Built in that is true if all values of a string are numbers
            hasNum = True 
    return hasNum

def checkLength(userInput): # Verify  user input is >= 8 characters long
    longEnough = False
    if len(userInput) < 8:
        longEnough = False
    else:
        longEnough = True
    return longEnough

def checkUpper(userInput): # Verify  user input has a upper-case letter in it
    hasUpper = False
    for letter in userInput: 
        if letter.isupper(): # Built in that is true if all values of a string are upper-case letters
            hasUpper = True
    return hasUpper

def checkLower(userInput): # Verify  user input has a lower-case letter in it
    hasLower = False
    for letter in userInput: 
        if letter.islower(): # Built in that is true if all values of a string are lower-case letters
            hasLower = True
    return hasLower

def checkSpecial(userInput): # Verify  user input has a special character in it
    hasSpecial = False
    special = '''!@$%^&*()_-+={[}]|\\:;"'<,>.\\#'''
    for letter in userInput:
        if letter in special:
            hasSpecial = True
    return hasSpecial

def passCheck(req1, req2, req3, req4, req5): # Verify password requirements and inform user of insufficiencies
    goodPass = False
    if req1 is False:
        print("\nPlease ensure password contains a number")
    elif req2 is False:
        print("\nPlease ensure password is at least 8 characters long")
    elif req3 is False:
        print("\nPlease ensure password contains a upper-case letter")
    elif req4 is False:
        print("\nPlease ensure password contains a lower-case letter")
    elif req5 is False:
        print('''\nPlease ensure password contains a special character\nSpecial Characters are as follows\n ! @ $ % ^ & * ( ) - _ = + } ] { [ \\ | : ; " ' < . > /\\# , ?\n''')
    else:
        goodPass = True
        print("\nPassword set successfully") # Display that user password was accepted
    return goodPass

def displayCheck(password):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    special = '''!@$%^&*()_-+={[}]|\\:;"'<,>.\\#'''
    for character in password:
        if password in upper and lower and number and special:
            print("Password:",password)
            print()
            return password
            
def retry(): # Prompt user to retry input if criteria is not met
    retry = input("Try again:\n")
    return retry

def verifyer(userIn):
    userInput = removeSpace(userIn)
    check1 = checkNumber(userInput)
    check2 = checkLength(userInput)
    check3 = checkUpper(userInput)
    check4 = checkLower(userInput)
    check5 = checkSpecial(userInput)
    goodPass = passCheck(check1, check2, check3, check4, check5)

    if goodPass:
        print("Password:", userInput)
        print()
        return userInput
    else:
        while goodPass is False:
            attempt2 = retry()
            verifyer(attempt2) # Prompt user to retry input if criteria is not met
            displayCheck(attempt2) # only print input that resulted in a strong password
            return attempt2
            break # Turn off/stop the "while" loop once password requirements are satisfied


def prompt_userFirst(): #Asks the user to enter their name & returns lowercase value to be used when forming username
    first_name = input("Please enter your first name: ")
    lowercase_first = first_name.lower()
    #print()
    return lowercase_first

def prompt_userLast(): #Asks the user to enter their last name & returns lowercase value to be used when forming username
    last_name = input("Please enter your last name: ")
    lowercase_last = last_name.lower()
    print()
    return lowercase_last

def prompt_dob(): #Asks the user for their date of birth
    dob = input("Please enter your date of birth using Month/Day/Year: ")
    print()
    return dob

def check_fname(lowercase_fname): #Checks that the first names truth value (must be empty of special characters and numbers). True/False will be used to determine whether to prompt the user again or use the input given
    hasDigit = False
    hasSpecial = False
    special = '''!@$%^&*()_-+={[}]|\\:;"'<,>.\\#'''
    for letter in lowercase_fname:
        if letter.isdigit():
            hasDigit = True
            break
    for letter in lowercase_fname:
        if letter in special:
            hasSpecial = True
            break
    return hasDigit, hasSpecial

def check_lname(lowercase_lname): #Checks truth value for last name validity(must be empty of special characters and numbers). True/False will be used to determine whether to prompt the user again or use the input given
    hasDigit = False
    hasSpecial = False
    special = '''!@$%^&*()_-+={[}]|\\:;"'<,>.\\#'''
    for letter in lowercase_lname:
        if letter.isdigit():
            hasDigit = True
            break
    for letter in lowercase_lname:
        if letter in special:
            hasSpecial = True
            break
    return hasDigit, hasSpecial

def check_dob(dob): #Checks truth value for date of birth validity, allows only digits and '/'. True/False will be used to determine whether to prompt the user again or use the input given
    invalid = False
    for char in dob:
        if not (char.isdigit() or char == '/'):
            invalid = True
            break
    return invalid

def get_valid_first_name(): #Checks if True that first name has special char/numbers. If True, re-prompts user for first name. If otherwise, a valid first name is returned
    while True:
        first_name = prompt_userFirst() #Re-prompts user if True
        fname_digit, fname_special = check_fname(first_name)
        if fname_digit or fname_special:
            print("Error: First name must contain only letters (no numbers or special characters). Please try again.")
            print()
        else:
            return first_name

def get_valid_last_name(): #Checks if True that last name has special char/number. If True, re-prompts user for last name. If otherwise, a valid last name is returned
    while True:
        last_name = prompt_userLast()   #Re-prompts user if True
        lname_digit, lname_special = check_lname(last_name)
        if lname_digit or lname_special:
            print("Error: Last name must contain only letters (no numbers or special characters). Please try again.")
            print()
        else:
            return last_name

def get_valid_dob(): # Checks if True that DOB has special char or letter. If True, re-prompts user for DOB
    while True:
        dob = prompt_dob() # Re-prompts user if True 
        if dob.count('/') != 2: # Check that DOB contains exactly two '/' characters.
            print("Error: Date of birth must be in the format Month/Day/Year with '/' between each value. Please try again.")
            print()
            continue
        if check_dob(dob):
            print("Error: Date of birth must contain only numbers and '/' (no letters or special characters). Please try again.")
            print()
            continue
        return dob


def encrypt(data):
    import random
    key = random.randint(1, 255)  # Sets the encryption key to a random integer between 1-255
    encrypted_data = ''.join(chr((ord(char) + key) % 256) for char in data)  # Converts all characters to their number values, then adds the value of the random "key" to this number. If between 0-255 it then converts this number back into a character and writes this encoded version to the text files
    with open("passwords.txt", 'a', encoding="utf-8") as file: # Makes the type of encoding used "UTF-8" which is most common
        file.write(str(key) + "\n")  # Stores the encryption key
        file.write(encrypted_data + "\n") # Writes encrypted data to file
    return encrypted_data


# Pseudocode for decrypt_all:
#
#
# Unlike "prompt_decryption", "decrypt_all" can be used in a loop, as it doesnt open passwords.txt at the start of each iteration. Opening passwords.txt every time results in the same line being printed over and over.
#
# Steps:
#
# 1: Cycles through every character in encryption_data string. (for char in encryption_data)
# 2: Retrieves unicode# for each character w/ ord(char)
         # The characters are the ones resulting from "encrypt()", where each character was made unicode, had a random key added to it to produce a new unicode value, then converted the new unicode back into a new unique character
# 3: Substracts the Key from the unicode value of the character, providing the original unicode of the unencrypted characters                                                                                           
         # Subtracting the Key will reverse encryption by providing the original characters unicode number, which then provides the original
# 4: Uses % 256 to make sure the result is between 0-255
     # This ensures the number is still an 8 bit value. UTF-8 Encoding uses 8-bit
# 5: Converts the resulting integer into a character value using: "chr" EG: chr((ord(char) - key) % 256)                                                                                       

                                                                                              

def decrypt_all(key, encryption_data):                                                 
    decrypted_data = ''.join(chr((ord(char) - key) % 256) for char in encryption_data)
    return decrypted_data                                                                                                                                   

def prompt_decryption():
    loginList = []
    with open("passwords.txt", "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()] # Removes blank lines so that they dont interfere with the steps in the loop
        for i in range(0, len(lines), 2): # Starts at 0, ends at the last line, and uses steps of 3 to print key, username, password
            try:
                key = int(lines[i])
                encryption_data = lines[i + 1]
                decrypted_data = decrypt_all(key, encryption_data)
                loginList.append(decrypted_data)
            except (ValueError, IndexError):
                continue
        return loginList

def dataFormatter(loginData):
    logins = []
    for element in loginData:
        login = element.split(",", 1)
        logins.append(login)
    return logins

def loginScreen(loginData):
    import sys
    while True:
        user = input("Please enter username: ")
        user_found = False
        for login in loginData:
            if login[0] == user:
                user_found = True
                while True:
                    password = input("Please enter password for this account: ")
                    if login[1] == password:
                        
                        print("Login Successful. Welcome to the student portal")
                        print()
                        print("[Imaginary Student Portal]")
                        print()
                        print()
                        return
                    else:
                        print("Invalid password")
        if not user_found:
            print("Invalid username")

def chooserBoi():
    while True:
        choice = removeSpace(input("1 - Administrator Login: \n2 - Student Login: \n3 - New Student Account: \n"))
        if choice in ('1', '2', '3'):
            return choice
        else:
            print("\nPlease make a selection by entering '1', '2', or '3':\n")

def newStudent():
    print("Please see below to create your account:\n")
    print()
    lowercase_first = get_valid_first_name() # Get only the invalid fields again until all are valid.
    lowercase_last = get_valid_last_name()
    dob = get_valid_dob()
    parts = dob.split('/') # Built in function that splits a string into a number of parts based on a seperator (in this case the seperator is the "/")
    year = parts[2] if len(parts) == 3 else ""
    username = lowercase_first + lowercase_last + year
    print("\nYour assigned username is: " + username + "\n")
    password = verifyer(userPass())
    login = username + "," + password
    encrypt(login)

    
#with open("passwords.txt", 'a', encoding="utf-8") as file: # Ensures UTF-8 coding. Without this the encoding encounters an error
#    file.write(encryption_data + "\n") # Writes the encrypted username and password to the file. "\n" used to create a new line in the text

def main():
    while True:
        choice = chooserBoi()
        if choice == '1':
            adminPin = input("Please enter administrator PIN: ")
            while adminPin != administratorPin:
                adminPin = input("Incorrect PIN. Please re-enter: ")
            import random
            classSize = display()
            if classSize == 0:
                try:
                    logins = prompt_decryption()
                    loginList = dataFormatter(logins)
                    print('\nCurrent Logins: ', *loginList, sep = '\n')
                except Exception:
                    print("\nNo accounts have been created yet.\n")
            else:
                for i in range(classSize):
                    print("Please see below to create account for Student", i + 1)
                    lowercase_first = get_valid_first_name()
                    lowercase_last = get_valid_last_name()
                    dob = get_valid_dob()
                    parts = dob.split('/')
                    year = parts[2] if len(parts) == 3 else ""
                    username = lowercase_first + lowercase_last + year
                    print("\nYour assigned username is: " + username + "\n")
                    password = verifyer(userPass())
                    login = username + "," + password ### Changed order it is written to file so username is first

                    encrypt(login)
                
        elif choice == '2':
            try:
                logins = prompt_decryption()
                loginList = dataFormatter(logins)
                credentials = loginScreen(loginList)
            except Exception:
                print("\nError: \n\nNo accounts have been created yet")
                
        elif choice == '3':
            newStudent()

        exit_choice = input('Would you like to exit the program? If yes enter, "Y". To return to the home screen, enter "N" (Y/N): ')
        if exit_choice.lower() == 'y':
            break
    
main()
