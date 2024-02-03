import random
import string

def password_generator(min_length,numbers=True,special_char=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_char:
        characters+=special
    
    pwd=""
    meet_criteria=False
    has_number=False
    has_special=False

    while len(pwd) < min_length or (numbers and not has_number) or (special_char and not has_special):
        new_char=random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
    return pwd


min_length=int(input("Enter the length of password you require: "))
has_number=input("Enter yes,if you want to include numbers in password else,no? ").lower()=='yes'
has_special=input("Enter yes,if you want to include special characters in your password else,no? ").lower()=='yes'
pwd=password_generator(min_length,has_number,has_special)
print("Your password is: ",pwd)