chai_types = {
    "Masala": "Spicey",
    "Ginger": "zestey",
    "Green": "mild",
    "White": "sweet"
}
# print(chai_types["Green"])
# print(chai_types.get("Ginger"))

chai_types["White"] = "Fresh"
# print(chai_types)

# loop
# for chai in chai_types:
#     print(chai, chai_types[chai])

# for key, value in chai_types.items():
#     print(key, value)

# if "Masala" in chai_types:
#     print("I have Masala chai")

chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

chai_types.pop("Ginger")
chai_types.popitem()
del chai_types["Green"]
# print(chai_types)

# copy()
chai_types_copy = chai_types.copy()
# print("chai_types_copy: ", chai_types_copy)

tea_shop = {
    "chai": {"Masala": "Spicey", "Ginger": "Zesty"},
    "Tea": {"Black": "Strong", "Green": "Mild"}
}
# print(tea_shop)
# print(tea_shop["chai"])
# print(tea_shop["chai"]["Masala"])

squared_nums = {x:x**2 for x in range(10)}
# print(squared_nums)
squared_nums.clear()
# print(squared_nums)

keys = ["Masala", "Ginger", "Oolong"]
default_value = "Delicious"

# new_dict = dict.fromkeys(keys, default_value)
# new_dict = dict.fromkeys(keys, keys) 
# print(new_dict)
