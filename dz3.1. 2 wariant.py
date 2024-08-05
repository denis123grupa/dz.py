one = int(input('enter your 1 number:'))
two = int(input('enter your 2 number:'))
operation = input('enter your operation')

if operation == "+":
    print('a + b =', one + two)
elif operation == "-":
    if two == 0:
        print('Eror')
    else:
        print('a - b =', one - two)
elif operation == "*":
    print('a * b =', one * two)
else:
    print('a / b =', one / two)
