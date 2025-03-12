Encryption and decryption work well but some changes/improvements could be made:

1: Add prompt to ask if user would like to store logins, or retrieve(decrypt) logins

2: Option for user to specify which logins to decode & print

3: Need to re-prompt user for the # of students in the class instead of ending program when invalid input is given

4: Needs to prompt which username and password combination to decrypt instead of decrypting the whole file.
     - Can separate passwords written to file by lines using \n (one line per user+pass combo)
          - Python can detect lines within a text file which might allow us to decrypt user & password by specifying its line number in the text file
     - Might be able to do so with index #s
     - Might be able to require user to request by username
     - Could prompt user to give the username and password a label (eg. "gmail" or "youtube")

5: Include way to delete login information from the text file
