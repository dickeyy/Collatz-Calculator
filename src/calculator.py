# This is the Collatz conjecture.
# The conjecture states that if you take any positive integer, 1-infinity,
# and apply two simple rules to it, those rules being 
# if the number you have is even then divide it by two, if its odd then multiply by three and add one
# you keep doing this with each new number that you get based of the result of the rule that you just applied,
# for example, 10, 10 is even so divide by 2 and you get 5 thats odd so times 3 add one is 16
# thats odd so divide by thats 4 divide by 2 again and you get 1 thats odd so multiply by 3 and add 1,
# but wait thats 4... see the loop? The conjecture states that all positive numbers will eventually 
# come back to this 4-2-1-4 loop after applying the two rules however many times. 
# So far mathmaticians have yet to find a number that breaks this rule and every numeber
# all the way up to like 260 quadrillion has been tested or something so, so far there isnt a number that goes
# against this conjecture. And that is the Collatz Conjecture

# The following python script is an algorithm developed by Kyle Dickey made to test any number you want for the 4-2-1-4 loop.

# --------------------------------------------------------------------------------------------------------------------------------- 

import time
import random as r

print("\n---------------- Collatz Calculator by Kyle Dickey ----------------")

# Get number to test from user
def getNum():
    print("\nInput a number, press 'r' for a random, or press 'q' to quit:")
    global num
    num = input()
    if num == 'q':
        print("\n---------------- Thank you for using ----------------\n\n")
        time.sleep(0.5)
        exit()
    elif num == 'r':
        num = r.randint(1,9999999999999999999999999999999999999999999999999999999)
    else:  
        num = int(num)
        if num <= 0:
            num =1
            pass

    print(f'\n\nStarting at: {num} \n\n')

getNum()

# Algorithm to test inputed number
def collatzAlgorithm(num):

    global runs
    runs = 0
    global start
    start = time.time()

    while True:
        runs += 1

        # If the number is even
        if (num % 2) == 0:
            num /= 2
            print(num)

            if num == 1:
                break
        
        # If the number is odd
        else:
            num *= 3
            num += 1
            print(num)

            if num == 1:
                break

collatzAlgorithm(num)

# Tell the user it finished and how long it took
def reportLoop(runs, num): 
    end = time.time()
    elapsedTime = end - start
    print(f"\nNumber Tested: {num}")
    print(f"\nLoop reached... \nCalculated {runs} numbers in {elapsedTime} seconds\n")

# Define Startup process
def startUp():
    reportLoop(runs, num)
    getNum()
    collatzAlgorithm(num)

# Run startup infinity until quit by user
while True:
    startUp()

# --------------------------------------------------------------------------------------------------------------------------------- 

# And that ladies and gentleman is the Collatz Collab testable using a custom built algorithm.
# The actual algorithm has some non-required code in it for the timer and stuff so it could be shorter,
# so realistically it could be about 10 lines of code,
# it also is probably not as optimized as it could be but its good enough. 
# this script also allows a user to test their own number or test a random number 