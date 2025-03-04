#
#Name: Malachi Karczmar
#Date: 03 March 2025
#Assignment: Final - Username Generator


#Problem statement:
#Write a program to automatically generate a username based on first name, last name, and date of birth
# - Must prompt user for first name, last name, and date of birth
# - Username must be stored along with password in a file (eg. must be stored in the PW manager)
# - Output assigned username to the user
# - Prompt user with error if incorrect criteria entered, and ask to re-enter (ex. no last name, no DOB.etc)
# - Names can not have numbers or special characters
# - Date of birth can not contain letters or special characters aside from "/". Must be entered in Day/Month/Year format (***Technically only need to prompt for the year***)

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
        else:
            return first_name

def get_valid_last_name(): #Checks if True that last name has special char/number. If True, re-prompts user for last name. If otherwise, a valid last name is returned
    while True:
        last_name = prompt_userLast()   #Re-prompts user if True
        lname_digit, lname_special = check_lname(last_name)
        if lname_digit or lname_special:
            print("Error: Last name must contain only letters (no numbers or special characters). Please try again.")
        else:
            return last_name

def get_valid_dob(): #Checks if True that DOB has special char or letter. If True, re-prompts user for DOB
    while True:
        dob = prompt_dob() #Re-prompts user if True 
        # Check that DOB contains exactly two '/' characters.
        if dob.count('/') != 2:
            print("Error: Date of birth must be in the format Month/Day/Year with '/' between each value. Please try again.")
            continue
        if check_dob(dob):
            print("Error: Date of birth must contain only numbers and '/' (no letters or special characters). Please try again.")
            continue
        return dob

def main():
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

    #logins = {username:password, username2:password2}   ###Put this in main just to have it there, havent implemented it at all - wanted to talk about how to implement

main()
