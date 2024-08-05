number_one_value = int(input('enter your number one value:'))
value_number_two = int(input('enter your number two vaule:'))
operation = (input('enter your operation:'))

if operation == "+":
    print('a + b = ', number_one_value + value_number_two )
elif operation == "-":
    print('a - b = ', number_one_value - value_number_two )
elif operation == "*":
    print('a * b =', number_one_value * value_number_two)
else:
    if value_number_two == 0:
        print('you cant divide by zero')
    else:
        print('a / b = ', number_one_value / value_number_two)
        