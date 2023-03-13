from logic_operation import LogicFunction


def main():
    logic_function = LogicFunction()
    # logic_function.handler_input_formula('!((!x1+x3)*!(x2*!x3))')
    function = input('Input formula: ')
    logic_function.handler_input_formula(function)
    logic_function.create_logic_table()
    logic_function.perfect_conjunctive_normal_form()
    logic_function.perfect_disjunctive_normal_form()
    logic_function.calculate_ratio()
    print(f'Function: {function}')
    print(f'Table:\n{logic_function.table_object}')
    print(
        f'Perfect conjunctive normal form: {logic_function.perfect_conjunctive_normal_form_formula}')
    print(
        f'Perfect conjunctive normal form in binary: {logic_function.perfect_conjunctive_normal_form_in_bynary}')
    print(
        f'Perfect conjunctive normal form in decimal: {logic_function.perfect_conjunctive_normal_form_in_decimal}')
    print(
        f'Perfect disjunctive normal form: {logic_function.perfect_disjunctive_normal_form_formula}')
    print(
        f'Perfect disjunctive normal form in binary: {logic_function.perfect_disjunctive_normal_form_in_bynary}')
    print(
        f'Perfect disjunctive normal form in decimal: {logic_function.perfect_disjunctive_normal_form_in_decimal}')
    print(f'Index: {logic_function.number_ratio}')


if __name__ == '__main__':
    main()
