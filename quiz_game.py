print("Welcome to my computer quiz!")

playing=input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit() #the quit() terminates immediately that means it will execute the next steps
print("Okay lets play :)")

score=0
answer=input("What is the full form of OS ? ")
if answer.lower()=="operating system":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is the full form of PSU ? ")
if answer.lower()=="power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is full form of SQL ? ")
if answer.lower()=="structured query language":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("One byte = how many no.of bits ? ")
if answer=="8":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is full form of GPU ? ")
if answer.lower()=="graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("Your score is: "+str(score)+"/5")

