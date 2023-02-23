from number import Numbers
import time


def main():
    while True:
        first_number_input = input('Введите первое число: ')
        second_number_input = input('Введите второе число: ')
        if '.' in first_number_input:
            float_number(first_number_input, second_number_input)
        else:
            int_number(int(first_number_input), int(second_number_input))


def float_number(first_number_input, second_number_input):
    numbers_in_binary = Numbers(first_number_input, second_number_input)
    print(f'Сумма: {numbers_in_binary.addition_floating_number()}')


def int_number(first_number_input, second_number_input):
    operation = input('Операции(+, -, *, /): ')
    if operation == '+':
        print(f'''({first_number_input}) + ({second_number_input}) = {Numbers(str(first_number_input), str(second_number_input)).add_two_numbers()}''')
        print(f'({-1*first_number_input}) + ({second_number_input}) = {Numbers(str(-1*first_number_input), str(second_number_input)).add_two_numbers()}')
        print(f'({first_number_input}) + ({-1*second_number_input}) = {Numbers(str(first_number_input), str(-1*second_number_input)).add_two_numbers()}')
        print(f'({-1*first_number_input}) + ({-1*second_number_input}) = {Numbers(str(-1*first_number_input), str(-1*second_number_input)).add_two_numbers()}')
    elif operation == '-':
        print(f'({first_number_input}) - ({second_number_input}) = {Numbers(str(first_number_input), str(-1*second_number_input)).add_two_numbers()}')
        print(f'({-1*first_number_input}) - ({second_number_input}) = {Numbers(str(-1*first_number_input), str(-1*second_number_input)).add_two_numbers()}')
        print(f'({first_number_input}) - ({-1*second_number_input}) = {Numbers(str(first_number_input), str(second_number_input)).add_two_numbers()}')
        print(f'({-1*first_number_input}) - ({-1*second_number_input}) = {Numbers(str(-1*first_number_input), str(second_number_input)).add_two_numbers()}')
    elif operation == '*':
        print(f'({first_number_input}) * ({second_number_input}) = {Numbers(str(first_number_input), str(second_number_input)).product()}')
        print(f'({-1*first_number_input}) * ({second_number_input}) = {Numbers(str(-1*first_number_input), str(second_number_input)).product()}')
        print(f'({first_number_input}) * ({-1*second_number_input}) = {Numbers(str(first_number_input), str(-1*second_number_input)).product()}')
        print(f'({-1*first_number_input}) * ({-1*second_number_input}) = {Numbers(str(-1*first_number_input), str(-1*second_number_input)).product()}')
    elif operation == '/':
        print(f'({first_number_input}) - ({second_number_input}) = {Numbers(str(first_number_input), str(second_number_input)).division_numbers()}')
        print(f'({-1*first_number_input}) - ({second_number_input}) = {Numbers(str(-1*first_number_input), str(second_number_input)).division_numbers()}')
        print(f'({first_number_input}) - ({-1*second_number_input}) = {Numbers(str(first_number_input), str(-1*second_number_input)).division_numbers()}')
        print(f'({-1*first_number_input}) - ({-1*second_number_input}) = {Numbers(str(-1*first_number_input), str(-1*second_number_input)).division_numbers()}')
    else:
        print('Такой операции не существует')


if __name__ == '__main__':
    main()
