import json
import time as t
from turtle import update
import matplotlib.pyplot as plt
import random as r

with open("RGPoints.json", "r") as f:  # reading a file
    data = json.load(f)  # deserialization

# Get number to start test
with open('RGLastNum.json', 'r') as openfile:

    # Reading from json file
    oNumUF = json.load(openfile)

oNum = oNumUF['number']
num = oNum
runs = 0
i = 0

while i < 1000:
    runs += 1
    # If the number is even
    if (num % 2) == 0:
        num /= 2
        print(num)

        if num == 1:
            # store last successful number
            plotNumR = r.randint(1,1000000000000000000000000000000000)
            xNumLabel = f"x-{oNum}"
            yNumLabel = f"y-{oNum}"

            lastSuccessWrite = {
                "number": oNum,
                "startedAt": t.strftime(r"%m/%d/%Y %H:%M:%S", t.localtime())
            }
            plotsWriteX = { 
                oNum: runs,
            }

            with open("RGPoints.json", "r+") as f:
                data = json.load(f)
                data.update(plotsWriteX)

            with open("RPoints.json", "w") as f:
                json_object2 = json.dumps(data, indent = 4)
                f.write(json_object2)

            # Serializing json 
            json_object = json.dumps(lastSuccessWrite, indent = 4)
  
            # Writing to .json
            with open("RGLastNum.json", "w") as outfile:
                outfile.write(json_object)

            oNum += 1
            num = oNum
            
            print(f"\nLoop Reached... next number is {num}\n runs: {runs}")
            i += 1
            runs = 0
            
    # If the number is odd
    else:
        num *= 3
        num += 1
        print(num)

        if num == 1:
            # store last successful number
            plotNumR = r.randint(1,1000000000000000000000000000000000)
            xNumLabel = f"x-{plotNumR}"
            yNumLabel = f"y-{plotNumR}"

            lastSuccessWrite = {
                "number": oNum,
                "startedAt": t.strftime(r"%m/%d/%Y %H:%M:%S", t.localtime())
            }

            plotsWriteX = { 
               oNum: runs,
            }

            with open("RGPoints.json", "r+") as f:
                data = json.load(f)
                data.update(plotsWriteX)

            with open("RGPoints.json", "w") as f:
                json_object2 = json.dumps(data, indent = 4)
                f.write(json_object2)

            # Serializing json 
            json_object = json.dumps(lastSuccessWrite, indent = 4)
  
            # Writing to .json
            with open("RGLastNum.json", "w") as outfile:
                outfile.write(json_object)

            oNum += 1
            num = oNum
            
            print(f"\nLoop Reached... next number is {num}\n runs: {runs}")
            i += 1
            runs = 0