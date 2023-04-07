def myFunc():

    userStr = str(input('Enter a string: '))
    varList = list(userStr)

    returnList = []


    for i in range(len(varList)):
        returnList.append(varList[i])
        returnList.append(varList[i])

    returnStr = ''.join(returnList)
    return(returnStr)


print(myFunc())