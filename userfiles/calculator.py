import os, time

os.system("clear")

while True:
    operation = input("Operation (+ for plus, - for minus, * for multply, / for divide, ** for to the power of, exit for back): ")
    if operation=="exit":
        print(os.getcwd())
        os.system("python3 desktop.py")
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        os.system("clear")

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        os.system("clear")

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        os.system("clear")

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        os.system("clear")

    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
        os.system("clear")

    else:
        print('You have not typed a valid operator, please run the program again.')
        time.sleep(1.5)
        os.system("clear")