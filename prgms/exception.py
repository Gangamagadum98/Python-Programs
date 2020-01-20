# 3 types of errors - 1. Compile time error (like syntax error-missing(:), spelling)
#2 Logical error - (code get compiled gives incorrect op by developer)
# 3 Runtime error- (code get compiled properly like division by zero end user given wrong i/p)

a=5
b=2

try:
    print('resource open')
    print(a/b)
    k=int(input('Enter a number'))
    print(k)

except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by Zero",e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong...")

finally:
    print("resource closed")
