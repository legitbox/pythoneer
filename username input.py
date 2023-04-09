# create inputs for the first numbers and store then in a variable
num1 = input("please input your first number: ")
num2 = input("please input your second number: ")

# converts the string into int to get the ability to use the variable in a calculation
num1 = int(num1)
num2 = int(num2)

#run the calculations for the numbers
addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2

print("the result of addition: ", addition)
print("the result of subtraction: ", subtract)
print("the result of multiplication: ", multiply)
print("the result of division: ", divide)
