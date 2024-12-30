try:
    num1 = int(input("Enter first number: "))
except ValueError:
    print("Please enter a valid number")
    exit()
num2 = num1 % 2
if num2 == 0:
    print("Even")
else:
    print("Odd")
