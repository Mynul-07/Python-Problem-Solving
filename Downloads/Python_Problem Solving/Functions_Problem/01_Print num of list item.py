
def print_cities(cities):
    print("The number of cities in the list is: ", len(cities))


cities = input("Enter a list of cities separated by space: ").split()
# print_cities(cities)


def print_list(cities):
    for city in cities:
        print(city, end=" ")


print_list(cities)
