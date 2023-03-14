import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '../lab2'))

from logic_operation import LogicFunction
from calculation_method import *

def main():
    logic_function = LogicFunction()
    logic_function.handler_input_formula('!((!x1+x3)*!(x2*!x3))')
    logic_function.create_logic_table()
    logic_function.perfect_conjunctive_normal_form()
    logic_function.perfect_disjunctive_normal_form()
    #print(logic_function.perfect_conjunctive_normal_form_formula)
    #print(logic_function.perfect_disjunctive_normal_form_formula)
    amount_of_arguments = len(logic_function.arguments)
    #translate_in_pdnf(glue_implicants('( !x1 * !x2 * x3 )+( !x1 * x2 * !x3 )+( !x1 * x2 * x3 )+( x1 * x2 * !x3 )'))
    #translate_in_pcnf(glue_implicants('( x1 + x2 + x3 )*( !x1 + x2 + x3 )*( !x1 + x2 + !x3 )*( !x1 + !x2 + !x3 )'))
    
    translate_in_pdnf(glue_implicants(logic_function.perfect_disjunctive_normal_form_formula))
    translate_in_pcnf(glue_implicants(logic_function.perfect_conjunctive_normal_form_formula))
if __name__ == '__main__':
    main()