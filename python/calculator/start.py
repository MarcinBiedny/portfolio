import calculator as c

calculator = c.Calculator()

operation_type = input("Please provide operation type. Allowed = ['+', '-', '*', '/']\n")

if operation_type in calculator.ALLOWED_OPERATION_TYPES:
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
    if retry_count == calculator.ALLOWED_RETRY_COUNT:
        print("Too many retries, quitting...")
        quit()

if operation_type == '+':
    calculated_value = calculator.add (first_number, second_number)

if operation_type == '-':
    calculated_value = calculator.substract (first_number, second_number)

if operation_type == '*':
    calculated_value = calculator.multiply (first_number, second_number)

if operation_type == '/':
    calculated_value = calculator.divide (first_number, second_number)

print('Calculated value = ' + str(calculated_value))