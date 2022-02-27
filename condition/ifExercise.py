'''
Price of house is a $1M
if buyer has good credit
  they need to put down 10%
otherwise
  they need to put down 20%
print the down payment
'''
'''
price = 1000000 
has_good_credit = True

if has_good_credit:
  print("we put down 10%")
else:
  print("we put down 20%")
print('you bill is a $' + str(price - price // 10))

'''

# refactoring
price = 1000000
has_good_credit = True

if has_good_credit:
  down_payment = 0.1 * price
else:
  down_payment = 0.2 * price 
print(f"Down Payment: ${down_payment}")