from multiprocessing.connection import wait
import time
# import the time module

  
# define the countdown func.
def main():
    user_workout = input("what would you like your workout to be:(weights or cardio)")
    if user_workout == 'weights':
        weights()
    elif user_workout == 'cardio':
        cardio()
def weights():
    print("Lets start your workout, We are going to do exercises in a set pattern which will allows us to get the most gains")
    print('CHest excerises')
    countdown(30)
    wait(30)
    print('leg excerises')
    countdown(30)
    print('back excerises')
    countdown(30)
    print('biceps excerises')
    countdown(30)

def cardio():
    print("Lets start your workout, We are going to do exercises in a set pattern which will allows you to shed the most calories")
    for i in range(3):
        print('CHest excerises')
        countdown(30)
        wait(30)
        print('leg excerises')
        countdown(30)
        print('back excerises')
        countdown(30)
        print('biceps excerises')
        countdown(30)
        print('long break')
        countdown(60)
    
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    