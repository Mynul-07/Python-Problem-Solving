# find the first non-repeated character in a string
str = input("Enter a string: ")

for char in str:
    if str.count(char) == 1:
        print(f"First non-repeated character: {char}")
        break
