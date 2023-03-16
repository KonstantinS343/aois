from prettytable import PrettyTable
import random

def table_method(formula, base_formula,form_of_formula, amout_values, table_data):
    create_table(amout_values, formula, table_data)
    
def create_table(amount_values, formula, table_data):
    amount_rows = len(amount_values)//2
    amount_columns = len(amount_values) - amount_rows
    table = PrettyTable()
    rows = create_line(amount_rows, amount_values[:amount_rows])
    columns = create_line(amount_columns, amount_values[-amount_columns:])
    table.field_names = [f'{"".join(amount_values[:amount_rows])}/{"".join(amount_values[-amount_columns:])}',
                        *[''.join(map(str, i)) for i in transform_dict_in_list(columns)]]
    
    temp = transform_dict_for_table(table_data)
    for i in rows:
        output = []
        for j in columns:
            temp_row = i | j
            for k in temp:
                if temp_row in k:
                   output.append(k[1])
                   break
        table.add_row([''.join(map(str, list(i.values()))),*output])
    print(table)

def transform_dict_for_table(table_data):
    table = []
    for i in table_data:
        table.append([{j:k for j,k in i.items() if j != 'i' and j!= 'f'}, list(i.values())[-2]])
    return table

def transform_dict_in_list(table_data):
    dict_in_list = []
    for i in table_data:
        dict_in_list.append(list(i.values()))
    return dict_in_list

def create_line(amount_arguments, values):
    columns = [{i: 0 for i in values}]
    #columns = [[0]*amount_arguments]
    for i in range(1, 2**amount_arguments):
        for j in range(amount_arguments-1, -1,-1):
            temp = columns[i-1].copy()
            index = list(temp.keys())[j]
            temp[index] = 0
            if temp not in columns:
                columns.append(temp)
                break
            temp[index] = 1
            if temp not in columns:
                columns.append(temp)
                break
    return columns
            

