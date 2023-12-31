# calculator - Perform operation type indicated by user input on two given numbers.


class Calculator:
    ALLOWED_OPERATION_TYPES = ["+", "-", "*", "/"]
    ALLOWED_RETRY_COUNT = 5

    def add(self, n1, n2):
        return n1 + n2

    def substract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2
