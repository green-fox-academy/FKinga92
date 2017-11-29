# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

expression = [x for x in input("Please type in the expression: ").split()]
operation = str(expression[0])
num1 = float(expression[1])
num2 = float(expression[2])
if operation != "+" and operation != "-" and operation != "*" and operation != "/" and operation != "%":
    print("Please enter one of the operators +, -, *, / or % as the first input")
elif len(expression) != 3:
    print("Please enter one operator followed by two numbers")
else:
    if operation == "+":
        print(str(num1) + " + " + str(num2) + " = " + str(float(num1) + float(num2)))
    elif operation == "-":
        print(str(num1) + " - " + str(num2) + " = " + str(float(num1) - float(num2)))
    elif operation == "*":
        print(str(num1) + " * " + str(num2) + " = " + str(float(num1) * float(num2)))
    elif operation == "/":
        print(str(num1) + " / " + str(num2) + " = " + str(float(num1) / float(num2)))
    elif operation == "%":
        print(str(num1) + " % " + str(num2) + " = " + str(float(num1) % float(num2)))
