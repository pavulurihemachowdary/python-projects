import random

def roll():
    roll=random.randint(2,6)
    return roll
lt=[]
while True:
    players=input("Enter the number of Players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            
            for i in range(players):
                name=input("Enter Player"+str(i+1)+" Name: ")
                lt.append(name)
            break
        else:
            print("Must be between (2-4)")
    else:
        print("Invalid!,Try again")
max_score=50
player_scores=[0 for _ in range(players)]
while max(player_scores)<max_score:
    for player_idx in range(players):
        current_score=0
        print("\n",lt[player_idx],"has started!\n")
        print('Your total score is:',current_score)
        while True:
            should_roll=input("would you like to roll?(y): ")
            if should_roll.lower()!='y':
                break
            value=roll()
            if value==1:
                print("You rolled a 1! and game is done")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a:",value)
            print("Your score is:",current_score)
        player_scores[player_idx]+= current_score 
        print("Your total score is:",player_scores[player_idx])
res_score=max(player_scores)
res_idx=player_scores.index(res_score)
print("\n",lt[res_idx],"has won the game with a score of:",res_score,"\n")