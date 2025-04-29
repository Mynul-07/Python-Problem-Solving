# Factorial calculation using a while loop
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial = factorial * num
    num = num - 1
print(f"Factorial is {factorial}")


# factorial calculation using a for loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(F"Factorial is {factorial}")


# factorial calculation using recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Enter a number: "))
factorial = factorial(num)
print(F"factorial is {factorial}")
