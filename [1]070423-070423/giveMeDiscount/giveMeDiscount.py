valPrice = float(input('Enter Item Price: '))
valDiscount = float(input('Enter Discount(%):'))

valDiscountedPrice = valPrice * (100 - valDiscount)/100
print(valDiscountedPrice)
