# counting positive and negative number

numbers = input("Enter elements separated by space:").split()
count_positive = 0
count_negative = 0
for num in numbers:
    if int(num) > 0:
        count_positive += 1
    else:
        count_negative += 1

print(
    f"Positive numbers: {count_positive}, Negative numbers: {count_negative}")
