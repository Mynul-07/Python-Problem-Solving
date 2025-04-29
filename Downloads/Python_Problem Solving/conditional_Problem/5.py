# Weather Activity Suggestion

weather = input("Enter the weather (sunny, rainy, snowy): ").lower()
if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"

print(f"Suggested activity: {activity}")
