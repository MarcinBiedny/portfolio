# calculator - Perform operation type indicated by user input on two given numbers.

# 1. get user inputs:
#   1a. get operation type
#       validation: allowed = ['+', '-', '*', '/']


ALLOWED_OPERATION_TYPES = ['+', '-', '*', '/']

def add(n1, n2):
    return n1+n2
def substract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operation_type = input("Please provide operation type. Allowed = ['+', '-', '*', '/']\n")
if operation_type in ALLOWED_OPERATION_TYPES:
    print(operation_type + ' operation is correct')
else:
    print(operation_type + ' operation is incorrect')

first_number = int(input("Please provide first number: \n"))
second_number = int(input("Please provide second number: \n"))

if operation_type == '+':
    calculated_value = add (first_number, second_number)

print('Calculated value = ' + str(calculated_value))