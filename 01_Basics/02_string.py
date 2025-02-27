# string is immutable, never change original object

chai = "Masala Chai"
first_char = chai[0]
print_masala = chai[0:6]

myList = "0123456789"

# slice()
# print(myList[:])
# print(myList[0:5])
# print(myList[0:])
# print(myList[:-1])
# print(myList[0:7:2]) # third parameter called hopping
# print("from last", myList[-1:])

# upper(), lower()
# print(chai.lower())
# print(chai.upper())

# strip()
username = "    sam    "
# print(username)
# print(username.strip())

# replace()
# print(chai.replace("Masala", "Mint"))
# print(chai)

# split() # convert into list or Array format
chai = "Masala, Ginger, Mint, Lemon"
# print(chai.split())
# print(chai.split(", ")) # differ is detect automatically space if not giving condition

# find()
chai = "Masala Chai"
# print(chai.find("Chai"))
# print(chai.find("chai")) # return -1 if not found

# count()
chai = "Masala Chai Chai Chai"
# print(chai.count("Chai"))

# format()
chai_type = "Lemon"
quantity = 2
order = "I Orderd {} cups of {} tea"
# print(order.format(quantity, chai_type))

# join() # convert list to str
chai_list = ["Masala", "Ginger", "Lemon", "Mint"]
convert_into_str = ", ".join(chai_list)
# print(convert_into_str)

# len()
chai = "Lemon Tea"
# print(len(chai))

# for letters in chai:
#     print(letters)

# raw string
path = "c:\\user\\pwd"
path_two = r"c:\user\pwd" # r means raw str as it was, solve problem while declaration path

# print(path)
# print(path_two)

