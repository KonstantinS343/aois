import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '../lab2'))

from logic_operation import LogicFunction
from calculation_method import *
from tabular_calculation_method import *
from table_method import *

TESTS = ['!((!x1+!x3)*(!x2*!x3))',
        '(!x1+x2)',
        '!(x1+x2)*!(!x2+!x3)',
        '!(x1*x2)+!(x2*x3)',
        '!((!x1+x3)*!(x2*!x3))'
]

def main():
    for i in TESTS:
        logic_function = LogicFunction()
        logic_function.handler_input_formula(i)
        logic_function.create_logic_table()
        logic_function.perfect_conjunctive_normal_form()
        logic_function.perfect_disjunctive_normal_form()
        amount_values = logic_function.arguments
        print('------------INPUT---------------')
        print(logic_function.perfect_disjunctive_normal_form_formula)
        print(logic_function.perfect_conjunctive_normal_form_formula)
        print('------------CALCULATION METHOD---------------')
        translate_in_pdnf(calaculation_method(logic_function.perfect_disjunctive_normal_form_formula))
        translate_in_pcnf(calaculation_method(logic_function.perfect_conjunctive_normal_form_formula))
        print('------------MCCLUSKEY METHOD---------------')
        translate_in_pdnf(tabular_calculation_method(*glue_implicants(logic_function.perfect_disjunctive_normal_form_formula)))
        translate_in_pcnf(tabular_calculation_method(*glue_implicants(logic_function.perfect_conjunctive_normal_form_formula)))
        print('------------KARNAUGH MAP---------------')
        translate_in_pdnf(table_method(*glue_implicants(logic_function.perfect_disjunctive_normal_form_formula), amount_values, logic_function.table_data))
        translate_in_pcnf(table_method(*glue_implicants(logic_function.perfect_conjunctive_normal_form_formula), amount_values, logic_function.table_data))
        print('\n')

if __name__ == '__main__':
    main()