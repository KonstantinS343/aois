from prettytable import PrettyTable
from copy import deepcopy

def tabular_calculation_method(formula_after_glue, base_formula,form_of_formula):
    return implicats_table(formula_after_glue, base_formula)
    
def implicats_table(formula_after_glue, base_formula):
    table = PrettyTable()
    table_data = []
    table.field_names = ['  ', *base_formula]
    for i in formula_after_glue:
        table.add_row([i,*[all([k in j for k in i])*'X' for j in base_formula]])
        table_data.append([all([k in j for k in i])*'X' for j in base_formula])
    
    print(table)
    #print(table_data)
    index_of_delete_row = delete_row(table_data)
    while index_of_delete_row:
        del formula_after_glue[index_of_delete_row]
        del table_data[index_of_delete_row]
        index_of_delete_row = delete_row(table_data)
    return formula_after_glue
    
def delete_row(table_data):
    can_delete_row = []
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
            can_delete_row.append(i)
    if can_delete_row:
        return table_data.index(can_delete_row[0])
    else:
        return None
            
    