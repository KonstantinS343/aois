from itertools import product
from prettytable import PrettyTable

class LogicFunction:
    
    def __init__(self) -> None:
        self.logic_formula: str = None
        self.table_object = PrettyTable()
        self.table_instance = []
        self.perfect_conjunctive_normal_form_formula: str = ''
        self.perfect_disjunctive_normal_form_formula: str = ''
        self.perfect_conjunctive_normal_form_in_bynary = []
        self.perfect_conjunctive_normal_form_in_decimal = [0]
        self.perfect_disjunctive_normal_form_in_bynary = []
        self.perfect_disjunctive_normal_form_in_decimal = [0]
        self.number_ratio = 0
    
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
        self.table_object.field_names = ['x1', 'x2', 'x3', 'f(sknf)', 'f(sdnf)', 'i']
        value_of_x1_x2_x3 = product(range(2), repeat=3)
        const = 128
        
        for i in value_of_x1_x2_x3:
            self.temp_logic_formula = self.logic_formula
            self.temp_logic_formula = self.temp_logic_formula.replace('x1', str(i[0]))
            self.temp_logic_formula = self.temp_logic_formula.replace('x2', str(i[1]))
            self.temp_logic_formula = self.temp_logic_formula.replace('x3', str(i[2]))
            self.table_object.add_row([i[0], i[1], i[2], int(eval(self.temp_logic_formula)), 
                                       int(eval(self.temp_logic_formula)), 
                                       const,])
            self.table_instance.append({
                'x1':i[0],
                'x2':i[1],
                'x3':i[2],
                'f':int(eval(self.temp_logic_formula)),
                'i':const,
            })
            const //=2 

    def perfect_conjunctive_normal_form(self):
        for i in self.table_instance:
            if i['f'] == 0:
                part_of_form = ' + '.join([values*'!'+keys for keys, values in i.items() if keys != 'f' and keys!= 'i'])
                self.perfect_conjunctive_normal_form_formula += f'( {part_of_form} )*'
        self.perfect_conjunctive_normal_form_formula = self.perfect_conjunctive_normal_form_formula[:-1]
        self.perfect_conjunctive_normal_form_in_number_form()
        
    def perfect_conjunctive_normal_form_in_number_form(self):
        temp = self.perfect_conjunctive_normal_form_formula.split()
        for i in range(0,len(temp)):
            if temp[i] == 'x1' or temp[i]=='x2' or temp[i] == 'x3':
                self.perfect_conjunctive_normal_form_in_bynary.append('0')
            elif temp[i] == '!x1' or temp[i] == '!x2' or temp[i]  == '!x3':
                self.perfect_conjunctive_normal_form_in_bynary.append('1')
            elif temp[i][0] == ')':
                self.perfect_conjunctive_normal_form_in_bynary.append('*')
        self.perfect_conjunctive_normal_form_in_bynary = ''.join(self.perfect_conjunctive_normal_form_in_bynary[:-1])
        self.perfect_conjunctive_normal_form_in_decimal = self.translate_in_decimal(self.perfect_conjunctive_normal_form_in_decimal,
                                                                                    self.perfect_conjunctive_normal_form_in_bynary)
        self.perfect_conjunctive_normal_form_in_decimal = map(str, self.perfect_conjunctive_normal_form_in_decimal)
        self.perfect_conjunctive_normal_form_in_decimal = '*('+', '.join(self.perfect_conjunctive_normal_form_in_decimal)+')'
        
    def translate_in_decimal(self, object, object_in_bynary):
        power_for_binary_number = 2
        index_of_decimal_digit = 0
        for i in object_in_bynary:
            if i == '*' or i == '+':
                power_for_binary_number = 2
                object.append(0)
                index_of_decimal_digit+=1
                continue
            object[index_of_decimal_digit]+=int(i)*(2**power_for_binary_number)
            power_for_binary_number-=1
        return object    
    
    def perfect_disjunctive_normal_form(self):
        for i in self.table_instance:
            if i['f'] == 1:
                part_of_form = ' * '.join([abs(values-1)*'!'+keys for keys, values in i.items() if keys != 'f' and keys!= 'i'])
                self.perfect_disjunctive_normal_form_formula += f'( {part_of_form} )+'
        self.perfect_disjunctive_normal_form_formula = self.perfect_disjunctive_normal_form_formula[:-1]
        self.perfect_disjunctive_normal_form_in_number_form()
        
    def perfect_disjunctive_normal_form_in_number_form(self):
        temp = self.perfect_disjunctive_normal_form_formula.split()
        for i in range(0,len(temp)):
            if temp[i] == 'x1' or temp[i]=='x2' or temp[i] == 'x3':
                self.perfect_disjunctive_normal_form_in_bynary.append('1')
            elif temp[i] == '!x1' or temp[i] == '!x2' or temp[i]  == '!x3':
                self.perfect_disjunctive_normal_form_in_bynary.append('0')
            elif temp[i][0] == ')':
                self.perfect_disjunctive_normal_form_in_bynary.append('+')
        self.perfect_disjunctive_normal_form_in_bynary = ''.join(self.perfect_disjunctive_normal_form_in_bynary[:-1])
        self.perfect_disjunctive_normal_form_in_decimal = self.translate_in_decimal(self.perfect_disjunctive_normal_form_in_decimal,
                                                                                    self.perfect_disjunctive_normal_form_in_bynary)
        self.perfect_disjunctive_normal_form_in_decimal = map(str, self.perfect_disjunctive_normal_form_in_decimal)
        self.perfect_disjunctive_normal_form_in_decimal = '+('+', '.join(self.perfect_disjunctive_normal_form_in_decimal)+')'
        
    def calculate_ratio(self):
        for i in self.table_instance:
            if i['f'] == 1:
                self.number_ratio += i['i'] 
        