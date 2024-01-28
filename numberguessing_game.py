import random

top_range=input("Type a number: ")


if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("Type a number larger than 0 next time")
        quit()
else:
    print("Type a number next time")
    quit()

random_number=random.randint(0,top_range) 
guesses=0 

while True:
    guesses+=1
    user_guess=input("Guess a number between the range: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time")
        continue
    if user_guess==random_number:
        print("You got it!!")
        break
    elif user_guess>random_number:
        print("you were above the number!!")
    else:
        print("you were below the number!!")
print("You got it in",guesses,"gusses")



 #the randrange() gives numbers between the mentioned bounds.

#the randint() similar to randrange() but also includes the upperbound 
