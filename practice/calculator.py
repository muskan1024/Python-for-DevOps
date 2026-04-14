num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

choice = input("Enter the operation you want to perform (Options are: +, -, *, /, %): ")

if choice == "+":
    ans = num1+num2
    print("Addition of", num1, "&", num2, "is:", ans)
elif choice == "-":
    ans = num1-num2
    print("Subtraction of", num1, "&", num2, "is:", ans)
elif choice == "*":
    ans = num1*num2
    print("Multiplication of", num1, "&", num2, "is:", ans)
elif choice =="/":
    print("Division of", num1, "&", num2, "is:", num1/num2)
elif choice =="%":
    print("Modulus of", num1, "&", num2, "is:", num1%num2)
else:
    print("Please enter a valid Option")
    