# Movie ticket pricing
day = input("Enter the day of the week: ").lower()
age = int(input("Enter yur age: "))

if day == "wednesday":
    if age <= 18:
        print("Ticket price: $10")
    else:
        print("Ticket price: $6")
else:
    if age <= 18:
        print("Ticket price: $12")
    else:
        print("Ticket price: $8")
