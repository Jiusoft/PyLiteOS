import os, time, runpy

os.system("cls" if os.name=="nt" else "clear")

while True:
    print("PySubOS Calculator\n")
    operation = input("Operation (+ for plus, - for minus, * for multply, / for divide, ** for to the power of, exit for back): ").strip()
    if operation=="exit":
        runpy.run_path(path_name="desktop.py")
    number_1 = int(input('Enter your first number: ').strip())
    number_2 = int(input('Enter your second number: ').strip())

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        input("Press Enter to Continue...")
        os.system("cls" if os.name=="nt" else "clear")

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        input("Press Enter to Continue...")
        os.system("cls" if os.name=="nt" else "clear")

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        input("Press Enter to Continue...")
        os.system("cls" if os.name=="nt" else "clear")

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        input("Press Enter to Continue...")
        os.system("cls" if os.name=="nt" else "clear")

    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
        input("Press Enter to Continue...")
        os.system("cls" if os.name=="nt" else "clear")

    else:
        print('You have not typed a valid operator, please run the program again.')
        time.sleep(1.5)
        os.system("cls" if os.name=="nt" else "clear")