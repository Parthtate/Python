# List are mutable, can be change

tea_varities = ["Black", "Green", "Oolong", "Mint"]
# print(tea_varities)
# print(tea_varities[0])
# print(tea_varities[1:3])

# tea_varities[1] = "Herbal"
# tea_varities[1:2] = "Herbal" # treated as a list
# tea_varities[1:2] = ["Herbal"] # treated as a single object
# print(tea_varities)

tea_varities[1:3] = ["Herbal", "Masala"]
# print(tea_varities)

# print(tea_varities[1:1])
tea_varities[1:1] = ["coffee", "black_coffee"]
# print(tea_varities)

tea_varities[1:3] = [] # Delete operation insert empty array
# print(tea_varities)

# for loop 
# for tea in tea_varities:
#     print(tea, end=", ")

tea_varities.append("Oolong")

# if "Oolong" in tea_varities:
#     print("\nI have Oolong Tea")

# pop()
tea_varities.pop()
# print(tea_varities)

# remove()
tea_varities.remove("Black")
# print(tea_varities)

# insert()
tea_varities.insert(1, "White")
# print(tea_varities)

# copy() 
tea_varities_copy = tea_varities.copy() # created a new reference copy for tea_varities_copy
tea_varities_copy.append("Lemon")
# print(tea_varities_copy)
# print(tea_varities)

# list comprehension 
# print(range(10)) # range decide until when print the object

squared_nums = [x**2 for x in range(10)] # print squared nums by index 9, 10 is excluded
# print(squared_nums)

cube_nums = [y**3 for y in range(5)]
# print(cube_nums)
