print("""
 _____________________
|  _________________  |
| | MichaelJonathan   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|""")

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

first_number = float(input("What's the first number?: "))
should_continue = True
while should_continue:
    print("+, -, *, /")
    while True:
        operation = input("Pick an operation: ")
        if operation in operations:
            break
        else:
            print("Invalid operational! Please Choose From +, -, *, /.")
    next_number = float(input("What's the next number?: "))
    hasil = operations[operation](first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {hasil}")
   
    choose = input(f"Type 'y' to continue calculating with {hasil}, or type 'n' to start a new calculation or type 's' to stop:")
    if choose == "y":
        first_number = hasil 
    elif choose == "n":
        print("\n" * 20)
        first_number = float(input("What's the first number?: "))
    else:
        should_continue = False



