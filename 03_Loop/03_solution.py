table_number = int(input("Enter any table number: "))

if table_number > 0:
    for i in range(1, 11):
        if i == 5:
            continue
            
        print(table_number, "x", i, "=", table_number*i)    
else:
    print("Please enter positive number!")

# 3 x 1 = 3
# 3 x 2 = 6

