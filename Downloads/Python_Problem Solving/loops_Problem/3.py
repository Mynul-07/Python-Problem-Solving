# Multiplication table printer
number = int(input("enter a number: "))
for i in range(1, 11):
    if i == 5:
        continue
    # print(f"{number} X {i} = {number * i}")
    print(number, 'X', i, '=', number * i)
