def calc():
    valInt1 = float(input('Enter a first value: '))
    valOp = str(input('Enter an operator(*, /, +, -): '))
    valInt2 = float(input('Enter a Second value: '))

    if valOp == '*':
        print(valInt1 * valInt2)
    elif valOp == '/':
        print(valInt1 / valInt2)
    elif valOp == '+':
        print(valInt1 + valInt2)
    elif valOp == '-':
        print(valInt1 - valInt2)
    else:
        print('Error - Uknown Operator')

calc()
