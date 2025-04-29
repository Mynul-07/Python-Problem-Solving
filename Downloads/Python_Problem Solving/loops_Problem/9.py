# list uniqueness checker
items = input("enter a list of items separated by spaces: ").split()

unique_item = []

for item in items:
    if item not in unique_item:
        unique_item.append(item)
    else:
        print(item, "is a duplicate item")
        break
