val = str(input('Enter Word:'))
count = 0
for i in range(len(val)):
    if val[i] == 'a' or val[i] == 'e' or val[i] == 'i' or val[i] == 'o' or val[i] == 'u':
        count += 1
print('Total vowels in' ,val,'=',count)