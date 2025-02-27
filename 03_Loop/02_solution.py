number = int(input("Enter any number: "))
even_number_sum = 0

for iteration in range(0, number+1):
    if iteration % 2 == 0:
        even_number_sum += iteration

print("Your Number is:", number, "\nSum of even number are:", even_number_sum)