# Grade Calculator
score = int(input("Enter your score: "))
if score >= 101 or score < 0:
    print("invalid score")
    exit()

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

print(f"Grade is: {grade}")
