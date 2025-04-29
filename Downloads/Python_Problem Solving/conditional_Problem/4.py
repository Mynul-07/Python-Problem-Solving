# fruit ripeness checker
# This program checks the ripeness of fruits based on their color and size.
fruit = input("Enter the fruit name:").lower()
if fruit == "banana":
    color = input("Enter the color of the banana: ").lower()
    if color == "green":
        print("Unripe banana")
    elif color == "yellow":
        print("Ripe banana")
    elif color == "brown":
        print("Overripe banana")

else:
    print("Unknown fruit")
