oNum = 1
num = oNum

while True:
    # If the number is even
    if (num % 2) == 0:
        num /= 2
        print(num)

        if num == 1:
            oNum += 1
            num = oNum
            print(f"\nLoop Reached... next number is {num}\n")
            
    # If the number is odd
    else:
        num *= 3
        num += 1
        print(num)

        if num == 1:
            oNum += 1
            num = oNum
            print(f"\nLoop Reached... next number is {num}\n")