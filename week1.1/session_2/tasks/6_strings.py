# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # OUTPUTS THE STRING
print(f"Modified String 1: {user_string.lower()}")# OUTPUTS IN LOWERCASE
print(f"Modified String 2: {user_string.upper()}")#OUTPUTS IN UPPERCASE
print(f"Modified String 3: {user_string.strip()}")#
print(f"Modified String 4: {user_string.replace('a', '@')}")#REPLACES EACH A WITH AS 
print(f"Modified String 5: {user_string.capitalize()}")#CAPITALIZES FIRST LETTER
print(f"Modified String 6: {user_string[::-1]}")#REVERSES THE WORD
print(f"Modified String 7: {user_string.title()}")# MAKES THE STRING A TITLE
print(f"Modified String 8: {len(user_string)}")#COUNTS THE AMOUNT OF CHARACTERS
print(f"Modified String 9: {user_string.find('a')}")#FINDS THE POSTION OF A
print(f"Modified String 10: {user_string.count('a')}")#CONTS THE NUMBER OF a's
print(f"Modified String 11: {user_string.startswith('Hello')}")
print(f"Modified String 12: {user_string.endswith('!')}")
print(f"Modified String 13: {user_string.isalnum()}")
print(f"Modified String 14: {user_string.isalpha()}")
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!