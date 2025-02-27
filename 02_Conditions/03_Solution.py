student_score = int(input("Please enter your marks here: "))

if student_score > 100:
    print("Invalid Entered Marks")
    exit()

if (student_score >= 90):
    print("Your Grade is A")
elif (student_score >= 80):
    print("Your Grade is B")
elif (student_score >= 70):
    print("Your Grade is C") 
elif (student_score >= 60):
    print("Your Grade is D")
else:
    print("Your Grade is F")    

