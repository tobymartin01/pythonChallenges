
def myFunc():

    val = str(input('Enter string of Xs and Os'))
    countX = 0
    countO = 0

    for i in range(len(val)):
        if val[i] == 'X' or val[i] == 'x':
            countX += 1
        elif val[i] == 'O' or val[i] == 'o':
            countO += 1

    if countO == countX:
        return True
    else:
        return False

print(myFunc())