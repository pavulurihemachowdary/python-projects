from playsound import playsound
import time

CLEAR="\033[2J" #An ASCI esc value that makes the terminal clear
CLEAR_AND_RETURN="\033[H" #returns the cursor to the home position and prints over what currently present

#clear_and_return can do the stuff like ,there is no going to new line after clearing the terminal
#it is present in the print statement where and keeps updating the value by clearing and returning the next one.


def alarm(seconds):
    time_elapsed=0

    print(CLEAR)

    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1
        time_left=seconds-time_elapsed
        minutes_left=time_left//60
        seconds_left=time_left%60
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("alaram_sound.mp3")
        #here :02d gives us the 2 digit kind of representation.2 digited with decimal.

minutes=int(input("Enter how many minutes to wait: "))
seconds=int(input("Enter how many seconds to wait: "))
total_sec=minutes*60+seconds

alarm(total_sec)