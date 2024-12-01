while True:
    number1 = input("Type a number: ")
    number2 = input("Type a number: ")
    operator = input("Type an operator: ")

    number1_float = 0
    number2_float = 0
    number_valids = False    

    try:
        number1_float = float(number1)
        number2_float = float(number2)
        number_valids = True

    except:
        number_valids = None

    if number_valids is None:
        print("One or both numbers are not valid!")
        #back to the beginning
        continue

    valid_operators = "+-*/"

    if operator not in valid_operators:
        print("Invalid operator!")
        continue

    if len(operator) > 1:
        print("Type only one operator!")
        continue

    print("Resolving the operation...")

    if operator == "+":
        print(f'{number1_float} + {number2_float} = ', number1_float + number2_float)
    elif operator == "-":
        print(f'{number1_float} - {number2_float} = ', number1_float - number2_float)
    elif operator == "*":
        print(f'{number1_float} * {number2_float} = ', number1_float * number2_float)
    elif operator == "/":
        print(f'{number1_float} / {number2_float} = ', number1_float / number2_float)
    else:
        print("Could not solve.")                

    response_exit = input("Quer sair? [S]im: ").lower().startswith("s")

    if response_exit:
        break
