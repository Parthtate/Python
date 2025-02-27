# Tuple are immutable, compare to list, list are mutable

tea_types = ("Ginger", "Oolong", "Black", "Earl grey")
# print(tea_types)
# print(tea_types[0])
# print(tea_types[1:])
# print(tea_types[-1])

# tea_types[0] = "Green" # TypeError: 'tuple' object does not support item assignment 
# print(len(tea_types))

more_tea = ("Herbal", "Masala")

all_tea = tea_types + more_tea
# print(all_tea)

if "Masala" in all_tea:
    print("I have Masala tea")

# print(more_tea.count("Masala"))
# print(more_tea.count("Masa"))
