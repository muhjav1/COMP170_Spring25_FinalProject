'''
Malachi Karczmar
COMP170
Final Project
03-10-25
'''
def display():
    classSize = int(input("Welcome to your class's account creator!\n\
    Please enter the class size: "))
    return classSize

def userPass(): # Get input from user and define password requirements
    userPass = str(input('''Please enter a password as described:\n- is at least 8 characters long\n- Contains at least one uppercase letter\n- Contains at least one lowercase letter\n- Contains at least one number\n- Contains at least one special character\nSpecial Characters are as follows\n ! @ $ % ^ & * ( ) - _ = + } ] { [ \ | : ; " ' < . > / , ?\n\nNote:\nSpaces will not be accepted as input and will be removed.\n '''))
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
    special = '''!@$%^&*()_-+={[}]|\:;"'<,>.'''
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
        print('''\nPlease ensure password contains a special character\nSpecial Characters are as follows\n ! @ $ % ^ & * ( ) - _ = + } ] { [ \ | : ; " ' < . > / , ?\n''')
    else:
        goodPass = True
        print("\nPassword set successfully") # Display that user password was accepted
    return goodPass

def displayCheck(password):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    special = '''!@$%^&*()_-+={[}]|\:;"'<,>.'''
    for character in password:
        if password in upper and lower and number and special:
            print("Password:   ", password)
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
        print("Password:   ", userInput)
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
    return lowercase_first

def prompt_userLast(): #Asks the user to enter their last name & returns lowercase value to be used when forming username
    last_name = input("Please enter your last name: ")
    lowercase_last = last_name.lower()
    return lowercase_last

def prompt_dob(): #Asks the user for their date of birth
    dob = input("Please enter your date of birth using Month/Day/Year: ")
    return dob

def check_fname(lowercase_fname): #Checks that the first names truth value (must be empty of special characters and numbers). True/False will be used to determine whether to prompt the user again or use the input given
    hasDigit = False
    hasSpecial = False
    special = '''!@$%^&*()_-+={[}]|\:;"'<,>.'''
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
    special = '''!@$%^&*()_-+={[}]|\:;"'<,>.'''
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

def get_valid_dob(): #Checks if True that DOB has special char or letter. If True, re-prompts user for DOB
    while True:
        dob = prompt_dob() #Re-prompts user if True 
        # Check that DOB contains exactly two '/' characters.
        if dob.count('/') != 2:
            print("Error: Date of birth must be in the format Month/Day/Year with '/' between each value. Please try again.")
            print()
            continue
        if check_dob(dob):
            print("Error: Date of birth must contain only numbers and '/' (no letters or special characters). Please try again.")
            print()
            continue
        return dob
#Encryption
def encrypt(data):
    import random
    """Encrypts data using a random integer and writes it to a file.

    Args:
        filename: The name of the file to write to.
        data: The string data to encrypt and write.
    """
    key = random.randint(1, 255)  # Generate a random encryption key
    encrypted_data = ''.join(chr((ord(char) + key) % 256) for char in data)
    #encryption_data = logins
    with open("passwords.txt", 'a', encoding="utf-8") as file:
        file.write(str(key) + "\n")  # Stores the encryption key
        file.write(encrypted_data + "\n")
    return encrypted_data
        
def decrypt(login_info):
    """Decrypts data read from a file.
    
    Args:
        login_info: The filename to read from.
    
    Returns:
        The decrypted string data.
    """
    with open(login_info, 'r', encoding="utf-8", errors="ignore") as file:  # Added encoding and errors
        key = int(file.readline().strip())  # Read the key from the first line
        encryption_data = file.readline().strip()
        decrypted_data = ''.join(chr((ord(char) - key) % 256) for char in encryption_data)
    return decrypted_data

def prompt_decryption():
    login_request = input("Would you like to retrieve your login information? Y / N?")
    if login_request.lower() == "y":
        decrypted_data = decrypt("passwords.txt")  # Use the filename as argument
        print("Your decrypted login information is: ", decrypted_data)
    
def main():
    import random
    classSize = display()
    for i in range(classSize):
        print("Please see below to create account for student", i + 1)
        # Get only the invalid fields again until all are valid.
        lowercase_first = get_valid_first_name()
        lowercase_last = get_valid_last_name()
        dob = get_valid_dob()

        parts = dob.split('/') #Built in function that splits a string into a number of parts based on a seperator (in this case the seperator is the "/")
        if len(parts) == 3: #Makes sure the DOB has three parts (month, day, year)
            year = parts[2]
        else:
            year = ""

        username = lowercase_first + lowercase_last + year  ####Realized there was 0 point for me to ask for full DOB. We can easily remove it but figured I'd leave it for the very small chance theres a use
        print("Your assigned username is: " + username)

        password = verifyer(userPass())
        login = username + "," + password ## Changed order it is written to file so username is first

        encryption_data = encrypt(login)

        with open("passwords.txt", 'a', encoding="utf-8") as file:
            file.write(encryption_data + "\n") 
            prompt_decryption()
        
        #with open("passwords.txt", "a") as file:
        #    file = file.write(login)
        #logins = {username:password, username2:password2}   ###Put this in main just to have it there, havent implemented it at all - wanted to talk about how to implement

         # Have this function call outside of main so the original prompt doesn't repeat    

main()
