import json
import time as t

# Get number to start test
with open('Collatz-Algorithm/src/lastSuccessful.json', 'r') as openfile:

    # Reading from json file
    oNumUF = json.load(openfile)

oNum = oNumUF['number']
num = oNum

while True:
    # If the number is even
    if (num % 2) == 0:
        num /= 2
        print(num)

        if num == 1:
            # store last successful number
            lastSuccessWrite = {
                "number": oNum,
                "startedAt": t.strftime(r"%m/%d/%Y %H:%M:%S", t.localtime())
            }
            
            # Serializing json 
            json_object = json.dumps(lastSuccessWrite, indent = 4)
  
            # Writing to .json
            with open("Collatz-Algorithm/src/lastSuccessful.json", "w") as outfile:
                outfile.write(json_object)

            oNum += 1
            num = oNum
            print(f"\nLoop Reached... next number is {num}\n")
            
    # If the number is odd
    else:
        num *= 3
        num += 1
        print(num)

        if num == 1:
            # store last successful number
            lastSuccessWrite = {
                "number": oNum,
                "startedAt": t.strftime(r"%m/%d/%Y %H:%M:%S", t.localtime())
            }

            # Serializing json 
            json_object = json.dumps(lastSuccessWrite, indent = 4)
  
            # Writing to .json
            with open("Collatz-Algorithm/src/lastSuccessful.json", "w") as outfile:
                outfile.write(json_object)

            oNum += 1
            num = oNum
            print(f"\nLoop Reached... next number is {num}\n")