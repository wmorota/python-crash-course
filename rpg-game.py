# A simple RPG game created on Python
import time

def start():
    start = input(">    Welcome to ______, Please type 'start' to enter the ______: ")
    if start != "start":
        start_try_again()
    else:
        time.sleep(0.5)
        print(">    Proceed with caution...")
        time.sleep(1.5)
        for i in range(3,0,-1):
            print(">             %d" % i)
            time.sleep(0.75)

def start_try_again():
    start = input(">    Do you not wish to enter the ____? Type 'start' to begin your story: ")
    if start != "start":
        start_try_again()
    else:
        time.sleep(0.5)
        print(">    Proceed with caution...")
        time.sleep(1.5)
        for i in range(3,0,-1):
            print(">             %d" % i)
            time.sleep(0.75)



def main():
    start()

    #while True:
    #    print("This prints once a minute.")
    #    time.sleep(0.5) # Delay for 1 minute (60 seconds).


main()
