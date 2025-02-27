# 5! = 5*4*3*2*1 (Factorial)

number = int(input("Enter any Number: "))
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print("Factorial of give number is:", factorial)    


