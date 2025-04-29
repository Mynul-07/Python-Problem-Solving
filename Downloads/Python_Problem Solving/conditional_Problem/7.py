# Coffee customization
order = input(
    "Enter your coffee order (e.g., medium, large, extra large): ").lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").lower()

if extra_shot == "yes":
    coffee = order + " coffee with an extra shot"
else:
    coffee = order + " coffee"

print(f"Your order: {coffee}")
