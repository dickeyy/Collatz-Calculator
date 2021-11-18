# The Collatz Calculator

This is an algorithm custom built by Kyle Dickey, used to test numbers against the simple rules of the Collatz Conjecture.

## Get started 
If you want to try the calculator for yourself, simply clone this repository and open up the file `/src/exe/CollatzCalculator.exe` (basically find the .exe file called CollatzCalculator.exe) and open it up, you will be prompted to enter a number and the algorithm will calculate it. Alternatively, you can clone the repo and run the collatzAlgorithm.py file and see all the steps the algorithm goes through, if you go with this option, you can also have it randomly choose a number if you dont feel like thinking.

## Sequential.py
There is also a file called Sequential.py (`src/sequetial.py`), in this file the algorithm goes through every number possible. It starts with 1 and will count up trying every number until it runs into a problem. This file is really not very useful since every number up to like 260 quadrillion has been tested but its a cool proof of concept and I imagine if you put it on a server and let it run forever eventually it may be useful. Only problem is, if the script ever stops then when it restarts it would start back at 1 unless you change the start number in the script. I may work in a system where it keeps track of its last successful number incase it crashes.

## What is the Collatz Conjecture?
 The conjecture states: You take any positive integer, 1-infinity, and apply two simple rules to it, those rules being if the number you have is even then divide it by two, if its odd then multiply by three and add one you keep doing this with each new number that you get based of the result of the rule that you just applied,
for example, **10**, 10 is even so divide by 2 and you get **5** thats odd so times 3 add one is **16** thats even so divide by 2 thats **4** divide by 2 again and you get **1** thats odd so multiply by 3 and add 1, but wait thats **4**... see the loop? The conjecture states that all positive numbers will eventually come back to this **4-2-1-4** loop after applying the two rules however many times. So far mathematicians have yet to find a number that breaks this rule and every number all the way up to like 260 quadrillion has been tested or something so, so far there isn't a number that goes against this conjecture. 

## About this Algorithm
This is likely not as efficient as it could be and there is probably some ways I messed up. Also, the algorithm could be a lot shorter (something like 10 lines total) but i included all the other stuff to communicate with the user and all that. All that being said, the algorithm does work and it will test any number you want in fractions of a second. 