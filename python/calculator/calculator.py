# calculator - Perform operation type indicated by user input on two given numbers.

# 1. get user inputs:
#   1a. get operation type
#       validation: allowed = ['+', '-', '*', '/']
#   1b. get first number
#       validation: number = integer
#   1c. get second number
#       validation: number = integer
# 2. make calculations
# 3. display the result

ALLOWED_OPERATION_TYPES = ['+', '-', '*', '/']
ALLOWED_RETRY_COUNT = 5

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

retry_count = 0

while operation_type == '/' and second_number == 0:
    print("Second number can't be 0")
    second_number = int(input("Please provide another second number: \n"))
    retry_count += 1
    if retry_count == ALLOWED_RETRY_COUNT:
        print("Too many retries, quitting...")
        quit()

if operation_type == '+':
    calculated_value = add (first_number, second_number)

if operation_type == '-':
    calculated_value = substract (first_number, second_number)

if operation_type == '*':
    calculated_value = multiply (first_number, second_number)

if operation_type == '/':
    calculated_value = divide (first_number, second_number)

print('Calculated value = ' + str(calculated_value))