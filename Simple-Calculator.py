num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Press 1 for addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division")
choice=int(input("Enter your choice between 1-4:"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("Invalid input")