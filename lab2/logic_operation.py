from itertools import product
from prettytable import PrettyTable
from typing import *


class LogicFunction:

    def __init__(self) -> None:
        self.arguments = set()
        self.logic_formula: str = None
        self.table_object: object = PrettyTable()
        self.table_data: List[str] = []
        self.perfect_conjunctive_normal_form_formula: str = ''
        self.perfect_disjunctive_normal_form_formula: str = ''
        self.perfect_conjunctive_normal_form_in_bynary: List[str] = []
        self.perfect_conjunctive_normal_form_in_decimal: List[int] = [0]
        self.perfect_disjunctive_normal_form_in_bynary: List[str] = []
        self.perfect_disjunctive_normal_form_in_decimal: List[int] = [0]
        self.number_ratio: int = 0

    def handler_input_formula(self, formula: str) -> None:
        formula: List[str] = [i for i in formula]
        for i in range(len(formula)):
            if formula[i] == '!':
                formula[i] = ' not '
            elif formula[i] == '+':
                formula[i] = ' or '
            elif formula[i] == '*':
                formula[i] = ' and '
            elif formula[i] == 'x':
                self.arguments.add(formula[i] + formula[i + 1])
            elif formula[i] == '=' and formula[i - 1] != ' =':
                formula[i] = ' ='
            elif formula[i] == '>':
                formula[i] = '> '
            elif formula[i] == '=' and formula[i - 1] == ' =':
                formula[i] = '= '
        self.logic_formula = ''.join(formula)
        for j in range(self.logic_formula.split().count('=>')):
            self.replace_implication()
        self.arguments = list(self.arguments)
        self.sort_argument()

    def replace_implication(self):
        formula = self.logic_formula.split()
        data_of_open_staples, implication = [''], False
        for i in range(len(formula) - 1, -1, -1):
            if formula[i] == '=>' and not implication:
                formula[i], implication = ') or', True
                formula[i - 1] += ')'
                if formula[i - 1][-1] != ')':
                    formula.insert(i - 1, ' (not( ')
                    break
            if data_of_open_staples and formula[i][0] == '(' and implication:
                if [x for x in formula[i]].count('(') > len(data_of_open_staples):
                    difference_between_staples = [x for x in formula[i]].count('(') - len(data_of_open_staples)
                    formula[i] = '(' * difference_between_staples + ' (not (' +''.join(formula[i][difference_between_staples:])
                    break
                data_of_open_staples[:] = [')' for j in range(0, len(data_of_open_staples) - [x for x in formula[i]].count('('))]
            if data_of_open_staples and formula[i][-1] == ')' and implication:
                data_of_open_staples += ')' * [j for j in formula[i]].count(')')
                if data_of_open_staples[0] == '':
                    data_of_open_staples.pop(0)
                    data_of_open_staples.pop(0)
            if implication and not data_of_open_staples:
                formula.insert(i, ' (not( ')
                break
        self.logic_formula = ' '.join(formula)

    def sort_argument(self):
        self.arguments.sort(key=lambda x: int(x[1]))

    def replace_argument_on_number(self, set_of_values):
        counter = 0
        for i in self.arguments:
            self.temp_logic_formula = self.temp_logic_formula.replace(
                i, str(set_of_values[counter]))
            counter += 1

    def create_logic_table(self) -> None:
        self.table_object.field_names = [
            *self.arguments, 'f(sknf)', 'f(sdnf)', 'i']
        values_of_arguments: List[Tuple(int)] = product(
            range(2), repeat=len(self.arguments))
        begin_index: int = 2**(2**(len(self.arguments)) - 1)

        for i in values_of_arguments:
            self.temp_logic_formula = self.logic_formula
            self.replace_argument_on_number(i)
            self.table_object.add_row([*i,
                                       int(eval(self.temp_logic_formula)),
                                       int(eval(self.temp_logic_formula)),
                                       begin_index,
                                       ])
            data_for_row = {self.arguments[x]: i[x]
                            for x in range(len(self.arguments))}
            data_for_row = {**data_for_row,
                            'f': int(eval(self.temp_logic_formula)),
                            'i': begin_index,
                            }
            self.table_data.append(data_for_row)
            begin_index //= 2

    def perfect_conjunctive_normal_form(self) -> None:
        for i in self.table_data:
            if i['f'] == 0:
                part_of_form: str = ' + '.join(
                    [values * '!' + keys for keys, values in i.items() if keys != 'f' and keys != 'i'])
                self.perfect_conjunctive_normal_form_formula += f'( {part_of_form} )*'
        self.perfect_conjunctive_normal_form_formula = self.perfect_conjunctive_normal_form_formula[:-1]
        self.perfect_conjunctive_normal_form_in_number_form()

    def perfect_conjunctive_normal_form_in_number_form(self) -> None:
        temp_perfect_conjunctive_normal: List[str] = self.perfect_conjunctive_normal_form_formula.split()
        for i in range(0, len(temp_perfect_conjunctive_normal)):
            if temp_perfect_conjunctive_normal[i][0] == 'x' or temp_perfect_conjunctive_normal[i][0] == 'x' \
                    or temp_perfect_conjunctive_normal[i][0] == 'x':
                self.perfect_conjunctive_normal_form_in_bynary.append('0')
            elif temp_perfect_conjunctive_normal[i][0] == '!' or temp_perfect_conjunctive_normal[i][0] == '!' \
                    or temp_perfect_conjunctive_normal[i][0] == '!':
                self.perfect_conjunctive_normal_form_in_bynary.append('1')
            elif temp_perfect_conjunctive_normal[i][0] == ')':
                self.perfect_conjunctive_normal_form_in_bynary.append('*')
        self.perfect_conjunctive_normal_form_in_bynary = ''.join(
            self.perfect_conjunctive_normal_form_in_bynary[:-1])
        self.perfect_conjunctive_normal_form_in_decimal = self.translate_in_decimal(
            self.perfect_conjunctive_normal_form_in_decimal,
            self.perfect_conjunctive_normal_form_in_bynary)
        self.perfect_conjunctive_normal_form_in_decimal = map(
            str, self.perfect_conjunctive_normal_form_in_decimal)
        self.perfect_conjunctive_normal_form_in_decimal = '*(' + ', '.join(
            self.perfect_conjunctive_normal_form_in_decimal) + ')'

    def translate_in_decimal(
            self,
            form_in_decimal: str,
            form_in_bynary: str) -> int:
        power_for_binary_number: int = len(self.arguments) - 1
        index_of_decimal_digit: int = 0
        for i in form_in_bynary:
            if i == '*' or i == '+':
                power_for_binary_number = len(self.arguments) - 1
                form_in_decimal.append(0)
                index_of_decimal_digit += 1
                continue
            form_in_decimal[index_of_decimal_digit] += int(i) * (2**power_for_binary_number)
            power_for_binary_number -= 1
        return form_in_decimal

    def perfect_disjunctive_normal_form(self) -> None:
        for i in self.table_data:
            if i['f'] == 1:
                part_of_form = ' * '.join([abs(values - 1) * '!' + keys for keys,
                                          values in i.items() if keys != 'f' and keys != 'i'])
                self.perfect_disjunctive_normal_form_formula += f'( {part_of_form} )+'
        self.perfect_disjunctive_normal_form_formula = self.perfect_disjunctive_normal_form_formula[:-1]
        self.perfect_disjunctive_normal_form_in_number_form()

    def perfect_disjunctive_normal_form_in_number_form(self) -> None:
        temp_perfect_disjunctive_normal: List[str] = self.perfect_disjunctive_normal_form_formula.split()
        for i in range(0, len(temp_perfect_disjunctive_normal)):
            if temp_perfect_disjunctive_normal[i][0] == 'x' or temp_perfect_disjunctive_normal[i][0] == 'x' \
                    or temp_perfect_disjunctive_normal[i][0] == 'x':
                self.perfect_disjunctive_normal_form_in_bynary.append('1')
            elif temp_perfect_disjunctive_normal[i][0] == '!' or temp_perfect_disjunctive_normal[i][0] == '!' \
                    or temp_perfect_disjunctive_normal[i][0] == '!':
                self.perfect_disjunctive_normal_form_in_bynary.append('0')
            elif temp_perfect_disjunctive_normal[i][0] == ')':
                self.perfect_disjunctive_normal_form_in_bynary.append('+')
        self.perfect_disjunctive_normal_form_in_bynary = ''.join(
            self.perfect_disjunctive_normal_form_in_bynary[:-1])
        self.perfect_disjunctive_normal_form_in_decimal = self.translate_in_decimal(
            self.perfect_disjunctive_normal_form_in_decimal,
            self.perfect_disjunctive_normal_form_in_bynary)
        self.perfect_disjunctive_normal_form_in_decimal = map(
            str, self.perfect_disjunctive_normal_form_in_decimal)
        self.perfect_disjunctive_normal_form_in_decimal = '+(' + ', '.join(
            self.perfect_disjunctive_normal_form_in_decimal) + ')'

    def calculate_ratio(self) -> None:
        for i in self.table_data:
            if i['f'] == 1:
                self.number_ratio += i['i']
