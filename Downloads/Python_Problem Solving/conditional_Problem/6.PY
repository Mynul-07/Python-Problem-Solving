# transportation mood selection

distance = int(input("Enter the distance in km: "))
if distance < 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
else:
    mode = "Car"

print(f"Suggested mode of transportation: {mode}")
