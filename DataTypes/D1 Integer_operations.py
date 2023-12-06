def perform_operation(operation, a, b):
    if operation == 'addition':
        return a + b
    elif operation == 'subtraction':
        return a - b
    elif operation == 'multiplication':
        return a * b
    elif operation == 'division':
        return a / b
    elif operation == 'floor_division':
        return a // b
    elif operation == 'modulus':
        return a % b
    elif operation == 'exponentiation':
        return a ** b
    elif operation == 'bitwise_and':
        return a & b
    elif operation == 'bitwise_or':
        return a | b
    elif operation == 'bitwise_xor':
        return a ^ b
    elif operation == 'bitwise_not':
        return ~a
    elif operation == 'bitwise_left_shift':
        return a << b
    elif operation == 'bitwise_right_shift':
        return a >> b
    else:
        return None


def print_result(operation, result):
    print(f"{operation.capitalize()}: {result}")


def integer():
    a = int(input("Enter the first integer (a): "))
    b = int(input("Enter the second integer (b): "))

    operations = [
        'addition', 'subtraction', 'multiplication', 'division',
        'floor_division', 'modulus', 'exponentiation', 'bitwise_and',
        'bitwise_or', 'bitwise_xor', 'bitwise_not', 'bitwise_left_shift',
        'bitwise_right_shift'
    ]

    for operation in operations:
        result = perform_operation(operation, a, b)
        print_result(operation, result)


if __name__ == "__main__":
    integer()
