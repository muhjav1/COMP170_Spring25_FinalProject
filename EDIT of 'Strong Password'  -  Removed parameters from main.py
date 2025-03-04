'''
Muhammad Javed
COMP 150

Problem Statement:
Write a program to prompt user to enter password as described below:
- is at least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Contains at least one special character

For each password entered, the program must display whether or not each of the requirements are satisfied.
You may also opt to display only the missing requirement(s).
The program continues running to ask the user to enter a new password until a valid password is entered.
If the password satisfies all the requirements, the program exits (after displaying it).
'''


def userPass(): ####### Changed from "userPass =..." to "userInput =..." # Get input from user and define password requirements
    userInput = str(input('''Please enter a password as described:\n- is at least 8 characters long\n- Contains at least one uppercase letter\n- Contains at least one lowercase letter\n- Contains at least one number\n- Contains at least one special character\nSpecial Characters are as follows\n ! @ $ % ^ & * ( ) - _ = + } ] { [ \ | : ; " ' < . > / , ?\n\nNote:\nSpaces will not be accepted as input and will be removed.\n '''))
    return removeSpace(userInput) ######## Removes spaces in function instead of main

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
            
def retry(): ####### Same thing as main but without the full text prompt from "userPass" again
        userInput = input("Try again:\n")
        check1 = checkNumber(userInput)
        check2 = checkLength(userInput)
        check3 = checkUpper(userInput)
        check4 = checkLower(userInput)
        check5 = checkSpecial(userInput)
        goodPass2 = passCheck(check1, check2, check3, check4, check5)
        if goodPass2:
            print("Password:   ", userInput)
            return True ####### Returns True value to main so that it knows goodPass is True now and doesnt need reprint "Try again:"
        return False ####### If goodPass isnt True, keeps retrying
       
def main():
    userInput = userPass() ####### Sets the userInput parameter to the return value of the userPass function
    check1 = checkNumber(userInput)
    check2 = checkLength(userInput)
    check3 = checkUpper(userInput)
    check4 = checkLower(userInput)
    check5 = checkSpecial(userInput)
    goodPass = passCheck(check1, check2, check3, check4, check5)
    if goodPass:            ####### Something I did made the old if/else/while statement not work so I fiddled with it until it worked again
        print("Password:   ", userInput)
        return ####### Stops program if good password is entered
    else:
        while not goodPass:  ####### Keeps calling retry() until it returns True. Once it returns True, program stops.
           goodPass = retry()
        return
   
main()


