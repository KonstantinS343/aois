from itertools import product
from prettytable import PrettyTable

class LogicFunction:
    
    def __init__(self) -> None:
        self.logic_formula: str = None
        self.table_object = PrettyTable()
        self.table_instance = []
        self.perfect_conjunctive_normal_form_formula: str = ''
        self.perfect_disjunctive_normal_form_formula: str = ''
    
    def handler_input_formula(self, formula):
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
            self.table_instance.append({
                'x1':i[0],
                'x2':i[1],
                'x3':i[2],
                'f':int(eval(self.temp_logic_formula))
            })

    def perfect_conjunctive_normal_form(self):
        for i in self.table_instance:
            if i['f'] == 0:
                part_of_form = '+'.join([values*'!'+keys for keys, values in i.items() if keys != 'f'])
                self.perfect_conjunctive_normal_form_formula += f'({part_of_form})*'
        self.perfect_conjunctive_normal_form_formula = self.perfect_conjunctive_normal_form_formula[:-1]
    
    def perfect_disjunctive_normal_form(self):
        for i in self.table_instance:
            if i['f'] == 1:
                part_of_form = '*'.join([abs(values-1)*'!'+keys for keys, values in i.items() if keys != 'f'])
                self.perfect_disjunctive_normal_form_formula += f'({part_of_form})+'
        self.perfect_disjunctive_normal_form_formula = self.perfect_disjunctive_normal_form_formula[:-1]
        