def perform_string_operation(operation, string):
    if operation == 'concatenation':
        return string + " Concatenated"
    elif operation == 'repetition':
        return string * 3
    elif operation == 'slicing':
        return string[1:4]
    elif operation == 'range_slicing':
        return string[2:]
    elif operation == 'membership':
        return 'e' in string
    elif operation == 'iteration':
        return [char for char in string]
    elif operation == 'length':
        return len(string)
    elif operation == 'string_formatting':
        return "Value: %s" % string
    elif operation == 'capitalize':
        return string.capitalize()
    elif operation == 'center':
        return string.center(20, '-')
    elif operation == 'count':
        return string.count('e')
    elif operation == 'encode':
        return string.encode('utf-8')
    elif operation == 'decode':
        return string.encode('utf-8').decode('utf-8')
    elif operation == 'endswith':
        return string.endswith('ed')
    elif operation == 'startswith':
        return string.startswith('Hello')
    elif operation == 'expandtabs':
        return string.expandtabs(4)
    elif operation == 'find':
        return string.find('l')
    elif operation == 'index':
        return string.index('l')
    elif operation == 'isalnum':
        return string.isalnum()
    elif operation == 'isalpha':
        return string.isalpha()
    elif operation == 'isdigit':
        return string.isdigit()
    elif operation == 'islower':
        return string.islower()
    elif operation == 'isupper':
        return string.isupper()
    elif operation == 'isnumeric':
        return string.isnumeric()
    elif operation == 'isspace':
        return string.isspace()
    elif operation == 'isprintable':
        return string.isprintable()
    elif operation == 'join':
        return '-'.join(string)
    elif operation == 'lower':
        return string.lower()
    elif operation == 'upper':
        return string.upper()
    elif operation == 'swapcase':
        return string.swapcase()
    elif operation == 'title':
        return string.title()
    elif operation == 'lstrip':
        return string.lstrip()
    elif operation == 'rstrip':
        return string.rstrip()
    elif operation == 'strip':
        return string.strip()
    elif operation == 'max':
        return max(string)
    elif operation == 'min':
        return min(string)
    elif operation == 'replace':
        return string.replace('l', 'X')
    elif operation == 'split':
        return string.split(' ')
    elif operation == 'splitlines':
        return string.splitlines()
    elif operation == 'zfill':
        return string.zfill(10)
    elif operation == 'maketrans':
        return str.maketrans('aeiou', '12345')
    elif operation == 'translate':
        translation_table = str.maketrans('aeiou', '12345')
        return string.translate(translation_table)
    elif operation == 'partition':
        return string.partition(' ')
    elif operation == 'rpartition':
        return string.rpartition(' ')
    elif operation == 'rfind':
        return string.rfind('l')
    elif operation == 'rindex':
        return string.rindex('l')
    elif operation == 'rjust':
        return string.rjust(20, '-')
    elif operation == 'rsplit':
        return string.rsplit(' ')

    else:
        return None

def print_string_result(operation, result):
    print(f"{operation.capitalize()}: {result}")

def String():
    input_string = input("Enter a string: ")

    string_operations = [
        'concatenation', 'repetition', 'slicing', 'range_slicing',
        'membership', 'iteration', 'length', 'string_formatting',
        'capitalize', 'center', 'count', 'encode', 'decode',
        'endswith', 'startswith', 'expandtabs', 'find', 'index',
        'isalnum', 'isalpha', 'isdigit', 'islower', 'isupper',
        'isnumeric', 'isspace', 'isprintable', 'join', 'lower',
        'upper', 'swapcase', 'title', 'lstrip', 'rstrip', 'strip',
        'max', 'min', 'replace', 'split', 'splitlines', 'zfill',
        'maketrans', 'translate', 'partition', 'rpartition',
        'rfind', 'rindex', 'rjust', 'rsplit']

    for operation in string_operations:
        result = perform_string_operation(operation, input_string)
        print_string_result(operation, result)

if __name__ == "__main__":
    String()
