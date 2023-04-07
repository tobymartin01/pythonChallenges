listMix = list(input('Enter mixed string: '))
listNum = []

for i in range(len(listMix)):
    if listMix[i].isdigit() == True:
        listNum.append(listMix[i])

print(listMix)
