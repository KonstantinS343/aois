from itertools import product
from prettytable import PrettyTable

class LogicFunction:
    
    def __init__(self) -> None:
        self.logic_formula: str = None
        self.table_object = PrettyTable()
    
    def handler_input_formula(self, formula):
        #!((x1+x3)*!(x2*x3))
        #not ((x1 or x3) and not (x2 and x3))
        formula = [i for i in formula]
        
        for i in range(len(formula)):
            if formula[i] == '!':
                formula[i] = ' not '
            elif formula[i] == '+':
                formula[i] = ' or '
            elif formula[i] == '*':
                formula[i] = ' and '
        self.logic_formula = ''.join(formula)
    
    def create_logic_table(self):
        self.table_object.field_names = ['x1', 'x2', 'x3', 'f']
        value_of_x1_x2_x3 = product(range(2), repeat=3)
        
        for i in value_of_x1_x2_x3:
            self.temp_logic_formula = self.logic_formula
            self.temp_logic_formula = self.temp_logic_formula.replace('x1', str(i[0]))
            self.temp_logic_formula = self.temp_logic_formula.replace('x2', str(i[1]))
            self.temp_logic_formula = self.temp_logic_formula.replace('x3', str(i[2]))
            self.table_object.add_row([i[0], i[1], i[2], int(eval(self.temp_logic_formula))])
        
        print(self.table_object)

    def perfect_conjunctive_normal_form(self):
        pass
    
    def perfect_disjunctive_normal_form(self):
        pass