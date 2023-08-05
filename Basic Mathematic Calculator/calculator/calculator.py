print("hi i can do basic mathematical operations")
while True:
    print('input which opertaion you want there are')
    operation = str(input('addition, subtraction, division, multiplication, square, square root '))
    if 'add' in operation:
        first_number = float(input('input the first number ' ))
        second_number = float(input('input the second number ' ))
        addition = (first_number + second_number)
        print('the answer for ', first_number, '+', second_number, '=', addition)
    elif 'subtract' in operation:
        first_number = float(input('input the first number ' ))
        second_number = float(input('input the second number ' ))
        print('the answer for ', first_number, '-', second_number, '=', first_number - second_number)
    elif 'multi' in operation:
        first_number = float(input('input the first number ' ))
        second_number = float(input('input the second number ' ))
        print('the answer for ', first_number, '*', second_number, '=', first_number * second_number)

    elif 'divi' in operation:
        first_number = float(input('input the first number ' ))
        second_number = float(input('input the second number ' ))
        print('the answer for ', first_number, '/', second_number, '=', first_number / second_number)

    elif 'root' in operation:
        sqaure_root = float(input('input the numeber that you want to be square rooted '))
        print('the answer for the square root of', sqaure_root, '=', sqaure_root ** 0.5)

    elif 'squ' in operation:
        sqaure = float(input('input the number you want to be squared '))
        print('the answer for the square of', sqaure, '=',sqaure ** 2)
    else:
        print('invalid operation try again')
    