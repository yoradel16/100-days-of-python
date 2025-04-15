from Assets import calculator_art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

#Start of the program
def calculator():
    print(calculator_art.logo)
    continue_calc = True

    n1 = float(input("What is the first number? "))

    while continue_calc:
        for key,value in operations.items():
            print(f"{key}\n")
        chosen_operation = input("Pick an operation: ")
        n2 = float(input("What is the next number? "))
        output = operations.get(chosen_operation)(n1, n2)
        print(f"{n1} {chosen_operation} {n2} = {output}")

        continue_with_result = input(f"Type 'y' to continue calculating with {output} or type 'n' to start a new calculation: ").lower().strip()
        if continue_with_result == 'y':
            n1 = output
        else:
            continue_calc = False
            calculator()

calculator()