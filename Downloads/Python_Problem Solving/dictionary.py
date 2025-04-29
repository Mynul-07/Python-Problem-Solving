chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
# print(chai_types)
# print(chai_types["Masala"])
# print(chai_types.get("Ginger"))
chai_types["Green"] = "Fresh"
print(chai_types)
for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key)

print(chai_types.popitem())

squared_num = {x: x**2 for x in range(6)}
print(squared_num)

keys = ["Masala", "Black", "Ginger"]
default_value = "Delicious"
# default_value = ["Delicious", "Strong", "Zesty"]

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
