#================================================================
""" Name : Sreeja S N
    Email Id : sreeja.sn7@gmail.com
    Date :- 13-Aug-2014
    Project No: 5"""
#================================================================
import re

#Validate the input
def validation_for_input(expression):

    text = expression.split()
    length_of_text = len(text)
    valid = True
    operator = 0
    # Check if the input is in correct format
    if length_of_text != 3:
        validation_message = 'Enter the input in format "operand operator operand'
        valid = False

    if valid:
        first_operand = text[0]
        operator = text[1]
        second_operand = text[2]
        a = re.search('\D+', first_operand)
        b = re.search('\D+', second_operand)
        #Validate the operands.The operands should be of decimal values
        if a:
            validation_message = 'The operands should be of decimal values'
            valid = False
        elif b:
            validation_message = 'The operands should be of decimal values'
            valid = False
        elif (second_operand == '0') & (operator == '/'):
            # Validate for the second operand. The second operand should not be zero while dividing
            validation_message = 'The second operand cannot be zero with division'
            valid = False


    if valid:
        # Check for valid operators
        if (operator.strip() != '+') & (operator.strip() != '*') & (operator.strip() != '/') & (operator.strip() != '-'):
            validation_message = 'Enter Valid operator +,-,*,/'
            valid = False
        else:
            validation_message = ''
            valid = True

    valid_ = [valid, validation_message]
    return valid_

# Calculate the input expression when inout entered correctly.
def calculate_expression(expression):
    text = expression.split()
    first_operand = float(text[0])
    operator = text[1]
    second_operand = float(text[2])

    if operator == '+':
        # Add operands when +
        result = first_operand + second_operand
    elif operator == '-':
        # Substract operands when -
        result = first_operand - second_operand
    elif operator == '/':
        # Divide operands when /
        result = first_operand / second_operand
    elif operator == '*':
        # Multiply operands when *
        result = first_operand * second_operand
    return result


# Main Program
while True:
    # Enter the input
    expression = raw_input('Enter input in the form (Operand Operator Operand):')
    # Validate the entered input
    message = validation_for_input(expression)

    if message[0]:
        # If the input expression is correct calculate the expression entered
        result = calculate_expression(expression)
        print result
        # Ask user to continue expression evaluation
        iterate = raw_input('Do you wish to continue (y or n) ?')
        # Stop the evaluation to stop further calculation
        if iterate == 'n':
            break
    else:
        # Print the validation message.
        print message[1]

