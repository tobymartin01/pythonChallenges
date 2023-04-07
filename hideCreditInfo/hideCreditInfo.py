valCredit = list(input('Enter Card Number:'))

valCreditHidden = valCredit
for i in range(12):
    valCreditHidden[i] = '*'

print(''.join(valCreditHidden))