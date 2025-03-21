**# Pseudocode for function "decrypt_all" (also largely applies to "encrypt()":**

**# Unlike "prompt_decryption", _"decrypt_all"_ can be used in a loop, as it doesnt open passwords.txt at the start of each iteration. Opening passwords.txt every time results in the same line being printed over and over.**

**# Steps:**
**# 1:** Cycles through every character in encryption_data string. _(for char in encryption_data)_
**# 2:** Retrieves unicode# for each character w/ _ord(char)_
         # The characters are the ones resulting from _"encrypt()"_, where each character was made unicode, had a random key added to it to produce a new unicode value, then converted the new unicode back into a new unique character
**# 3:** Substracts the Key from the unicode value of the character, providing the original unicode of the unencrypted characters                                                                                           
         # Subtracting the Key will reverse encryption by providing the original characters unicode number, which then provides the original
**# 4:** Uses _% 256_ to make sure the result is between 0-255
     # This ensures the number is still an 8 bit value. UTF-8 Encoding uses 8-bit
**# 5:** Converts the resulting integer into a character value using: _"chr"_ EG: _chr((ord(char) - key) % 256)_

**Extra notes:**
Function _"decrypt_all"_ takes two parameters: _"key"_ and _"encryption_data"_.
- It's called within _"prompt_decryption"_ function
- The Key parameter symbolizes the *encrypted* character stored in the text file. Defined within _"prompt_decryption"_
- "encryption_data" specifies which line of the text file to retrieve data from using "lines[i + 1]" and a loop. Defined within _"prompt_decryption"_
- Uses _"try"_ and _"except"_ which we cover next week but I read up on
