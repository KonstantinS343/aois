import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '../lab2'))

from logic_operation import LogicFunction
from calculation_method import *
from tabular_calculation_method import *
from table_method import *

expr_y4 = "(!x4*!x3*!x2*!x1)+(!x4*!x3*!x2*x1)+(!x4*!x3*x2*!x1)+(!x4*!x3*x2*x1)+(!x4*x3*!x2*!x1)+(!x4*x3*!x2*x1)+(!x4*x3*x2*!x1)"
expr_y3 = "(!x4*!x3*x2*x1)+(!x4*x3*!x2*!x1)+(!x4*x3*!x2*x1)+(!x4*x3*x2*!x1)"
expr_y2 = "(!x4*!x3*!x2*x1)+(!x4*!x3*x2*!x1)+(!x4*x3*!x2*x1)+(!x4*x3*x2*!x1)+(x4*!x3*!x2*x1)"
expr_y1 = "(!x4*!x3*!x2*!x1)+(!x4*!x3*x2*!x1)+(!x4*x3*!x2*!x1)+(!x4*x3*x2*!x1)+(x4*!x3*!x2*!x1)"

expr_b = "(!x1*!x2*x3)+(!x1*x2*!x3)+(!x1*x2*x3)+(x1*x2*x3)"
expr_d = "(!x1*!x2*x3)+(!x1*x2*!x3)+(x1*!x2*!x3)+(x1*x2*x3)"
h1 = '(!x1*!x2*!x3*!x4*x5)+(x1*x2*x3*x4*x5)+(!x1*x2*x3*x4*x5)+(x1*!x2*x3*x4*x5)+(!x1*!x2*x3*x4*x5)+(x1*x2*!x3*x4*x5)+(!x1*x2*!x3*x4*x5)+(x1*!x2*!x3*x4*x5)+(!x1*!x2*!x3*x4*x5)+(x1*x2*x3*!x4*x5)+(!x1*x2*x3*!x4*x5)+(x1*!x2*x3*!x4*x5)+(!x1*!x2*x3*!x4*x5)+(x1*x2*!x3*!x4*x5)+(!x1*x2*!x3*!x4*x5)+(x1*!x2*!x3*!x4*x5)'
h2 = '(!x1*!x2*!x3*!x4*x5)+(!x1*x2*x3*x4*x5)+(!x1*!x2*x3*x4*x5)+(!x1*x2*!x3*x4*x5)+(!x1*!x2*!x3*x4*x5)+(!x1*x2*x3*!x4*x5)+(!x1*!x2*x3*!x4*x5)+(!x1*x2*!x3*!x4*x5)'
h3 = '(!x1*!x2*!x3*!x4*x5)+(!x1*!x2*x3*x4*x5)+(!x1*!x2*!x3*x4*x5)+(!x1*!x2*x3*!x4*x5)'
h4 = '(!x1*!x2*!x3*!x4*x5)+(!x1*!x2*!x3*x4*x5)'

TESTS = [
    h1,
    h2, 
    h3,
    h4
]
      
def main():
    for i in range(len(TESTS)):
        logic_function = LogicFunction()
        logic_function.handler_input_formula(TESTS[i])
        logic_function.create_logic_table()
        logic_function.perfect_conjunctive_normal_form()
        logic_function.perfect_disjunctive_normal_form()
        amount_values = logic_function.arguments
        print(f'------------INPUT#{i+1}---------------')
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
        
def lab4_8421_and_substractor():
    name_of_test = '8421+9'
    for i in range(len(TESTS)):
        logic_function = LogicFunction()
        logic_function.handler_input_formula(TESTS[i])
        logic_function.create_logic_table()
        logic_function.perfect_conjunctive_normal_form()
        logic_function.perfect_disjunctive_normal_form()
        if i > 3:
            name_of_test = 'substractor'
        print(f'------------INPUT#{i+1}({name_of_test})---------------')
        print(logic_function.perfect_disjunctive_normal_form_formula)
        print(f'------------OUTPUT#{i+1}({name_of_test})---------------')
        translate_in_pdnf(tabular_calculation_method(*glue_implicants(logic_function.perfect_disjunctive_normal_form_formula)))
        print('\n')
        
def lab5_substractor():
    for i in range(len(TESTS)):
        logic_function = LogicFunction()
        logic_function.handler_input_formula(TESTS[i])
        logic_function.create_logic_table()
        logic_function.perfect_conjunctive_normal_form()
        logic_function.perfect_disjunctive_normal_form()
        print(f'------------INPUT#{i+1}(h{i+1})---------------')
        print(logic_function.perfect_disjunctive_normal_form_formula)
        print(f'------------OUTPUT#{i+1}(h{i+1})---------------')
        translate_in_pdnf(tabular_calculation_method(*glue_implicants(logic_function.perfect_disjunctive_normal_form_formula)))
        print('\n')

if __name__ == '__main__':
    #main()
    #lab4_8421_and_substractor()
    lab5_substractor()
