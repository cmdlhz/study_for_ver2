num1 = 3.123456789
num2 = 10.12345

## FORMAT METHOD & 3 digits
print('num2 is {1:.3} and num1 is {0:.3}'.format(num1, num2))

## USING "F-STRINGS" & 3 decimal digits
print(f'num2 is {num2:.3f} and num1 is {num1:.3f}')
