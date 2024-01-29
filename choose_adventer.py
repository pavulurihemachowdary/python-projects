name=input("Enter your name: ")
print("Hello ",name," welcome to adventer game.")

answer=input("You are on a dirty road to move furthur choose left or right to go,(left/right)? ")

if answer=="right":
    answer=input("Now you have come to a river type swim to swim or cross to cross the river,(swim/cross)? ")
    
    if answer=="swim":
        print("You are eaten by aligator,You loose!!")
   
    elif answer=="cross":
        answer=input("now there is a stranger ,type (yes/no) to talk? ")
        
        if answer=="yes":
            print("The stranger gave you gold,You won!!")
        
        elif answer=="no":
            print("You ignore the stranger,missed gold,You lost!!")
        
        else:
            print("Not a valid one,You loose!!")
    
    else:
        print("Not a valid one ,You loose!!")

elif answer=="left":
    print("You are eaten by a tiger,You lost!!")

else:
    print("Not a valid one,You lost!!")
