from logic import LogicFunction

def main():
    function = LogicFunction()
    function.handler_input_formula('!((!x1+!x3)*!(!x2*!x3))')
    function.create_logic_table()
    function.perfect_conjunctive_normal_form()
    function.perfect_disjunctive_normal_form()
    function.calculate_ratio()
    print(f'Table:\n{function.table_object}')
    print(f'Perfect conjunctive normal form: {function.perfect_conjunctive_normal_form_formula}')
    print(f'Perfect conjunctive normal form in binary: {function.perfect_conjunctive_normal_form_in_bynary}')
    print(f'Perfect conjunctive normal form in decimal: {function.perfect_conjunctive_normal_form_in_decimal}')
    print(f'Perfect disjunctive normal form: {function.perfect_disjunctive_normal_form_formula}')
    print(f'Perfect disjunctive normal form in binary: {function.perfect_disjunctive_normal_form_in_bynary}')
    print(f'Perfect disjunctive normal form in decimal: {function.perfect_disjunctive_normal_form_in_decimal}')
    print(f'Index: {function.number_ratio}')

if __name__ == '__main__':
    main()