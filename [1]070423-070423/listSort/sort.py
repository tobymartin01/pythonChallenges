
def sorting():

    inputList = input('Enter list of comma separated numbers here: ')
    inputSort = input('Sort by (asc, desc, none): ')

    inputList = [int(s) for s in inputList.split(',')]
    

    if inputSort == 'asc':
        print(sorted(inputList))
    elif inputSort == 'desc':
        print(sorted(inputList, reverse=True))
    elif inputSort == 'none':
        print(inputList)
    else:
        print('Error: no valid sorting method entered')

sorting()