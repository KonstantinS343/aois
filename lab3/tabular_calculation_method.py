from prettytable import PrettyTable
from copy import deepcopy
from calculation_method import *


def tabular_calculation_method(
        formula_after_glue,
        base_formula,
        form_of_formula):
    if len(formula_after_glue) == 0:
        return '0'
    while True:
        size = len(formula_after_glue)
        formula_after_glue, temp_base_formula, form_of_formula = connect_two_implicats(
            formula_after_glue, form_of_formula)
        if len(formula_after_glue[0]) == 1:
            formula_in_list = set([j for i in formula_after_glue for j in i])
            formula_in_list = delete_extra_arguments(list(formula_in_list))
            formula_after_glue = formula_in_list
        if size == len(formula_after_glue):
            break
        if len(formula_after_glue) == 0:
            return '0'
        size_of_implicat = len(formula_after_glue[0])
        for i in formula_after_glue:
            if len(i) != size_of_implicat:
                return implicats_table(formula_after_glue, base_formula)
    return implicats_table(formula_after_glue, base_formula)


def implicats_table(formula_after_glue, base_formula):
    table = PrettyTable()
    table_data = []
    table.field_names = ['  ', *base_formula]
    for i in formula_after_glue:
        table.add_row(
            [i, *[all([k in j for k in i]) * 'X' for j in base_formula]])
        table_data.append(
            [all([k in j for k in i]) * 'X' for j in base_formula])

    #print(table)
    index_of_delete_row = delete_row(table_data)
    while index_of_delete_row is not None:
        del formula_after_glue[index_of_delete_row]
        del table_data[index_of_delete_row]
        index_of_delete_row = delete_row(table_data)
    return formula_after_glue


def delete_row(table_data):
    for i in table_data:
        table_data_after_daleted_row = deepcopy(table_data)
        table_data_after_daleted_row.remove(i)
        amount_implicats = dict()

        for j in table_data_after_daleted_row:
            for k in range(0, len(j)):
                if k not in amount_implicats and j[k] == 'X':
                    amount_implicats[k] = 1
                elif k in amount_implicats and j[k] == 'X':
                    amount_implicats[k] += 1
        if len(amount_implicats) == len(table_data[0]):
            return table_data.index(i)
    return None
