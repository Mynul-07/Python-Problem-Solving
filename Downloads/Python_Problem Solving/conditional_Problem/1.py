# Age Group Categorization
# This program categorizes a person's age into different groups.
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Senior")
