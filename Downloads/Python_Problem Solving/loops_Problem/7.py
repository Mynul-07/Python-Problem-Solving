# validate input
while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("valid input")
        break
    else:
        print("invalid input")
