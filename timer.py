#import the time module 
import time

#input the time in seconds
seconds = input("Enter the time in no of secs: ")

#define the countdown timer function
def countdown_timer(seconds):
    while seconds:

        min = int(seconds/60)
        sec = int(seconds%60)

        timer = f'{min}:{sec}'

        print(timer, end='\r')
        time.sleep(1)
        seconds = seconds -1
    print('time up')

#function call
countdown_timer(int(seconds))

