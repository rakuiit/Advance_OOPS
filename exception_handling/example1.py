a=10
b=0

try:
    d=a/b
    print(d)
    print('Inside try')

except ZeroDivisionError:
    print('Division by zero not allowed')

else:
    print("Inside Else")

finally:
    print("inside finally")

print("rest of code ")