from prettytable import PrettyTable
import math

def table_method(formula, base_formula,form_of_formula, amount_values, table_data):
    create_table(amount_values, formula, table_data, form_of_formula)
    
def create_table(amount_values, formula, table_data, form_of_formula):
    amount_rows = len(amount_values)//2
    amount_columns = len(amount_values) - amount_rows
    table = PrettyTable()
    rows = create_line(amount_rows, amount_values[:amount_rows])
    columns = create_line(amount_columns, amount_values[-amount_columns:])
    table.field_names = [f'{"".join(amount_values[:amount_rows])}/{"".join(amount_values[-amount_columns:])}',
                        *[''.join(map(str, i)) for i in transform_dict_in_list(columns)]]
    
    temp = transform_dict_for_table(table_data)
    temp_table = []
    index = -1
    for i in rows:
        temp_table.append([])
        index+=1
        output = []
        for j in columns:
            temp_row = i | j
            for k in temp:
                if temp_row in k:
                   temp_table[index].append((temp_row, k[1]))
                   output.append(k[1])
                   break
        table.add_row([''.join(map(str, list(i.values()))),*output])
    print(table)
    if form_of_formula == 'pdnf':
        minimize_pdnf(temp_table)
    else:
        minimize_pcnf(temp_table)

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
# 0 0 0 1 
# 0 0 1 1
# 0 0 1 0
# 1 0 0 0         
def minimize_pcnf(table_data):
    temp = []
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            if table_data[i][j][1] == 0:
                temp.append(table_data[i][j])
                for k in range(3):
                    a = table_data[i+1][j]
                    while a == 0:
                        pass

def minimize_pdnf(table_data):
    output = [[]]
    for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                if all(check_one_group(table_data, i, j)):
                    output[-1].append((table_data[i][j], ))          
    output.append([])
    for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                result = check_two_group(table_data, i, j)
                choose_group(result[1], output[1], table_data[i][j])         
    output.append([])
    for i in range(len(table_data)):
            for j in range(len(table_data[i])):
                if all(check_one_group(table_data, i, j)):
                    output[-1].append(table_data[i][j])          
    print(output)   

def choose_group(result, output, current_element):
    if current_element not in [i[1] for i in output]:
        for i in result:
            if (i not in [i[0] for i in output] and i not in [i[1] for i in output]) or len(result) == 1:
                output.append((current_element, i))
# 0 0 0 1     
# 0 1 1 1
def check_one_group(table_data, current_row, current_column):
    top, bottom, left, right = False, False, False, False
    if table_data[current_row][current_column][1] == 1:
        if current_column != len(table_data[current_row])-1:
            if table_data[current_row][current_column+1][1] != 1:
                right = True
        elif table_data[current_row][0][1] != 1:
            right = True
        if current_column != 0:
            if table_data[current_row][current_column-1][1] != 1:
                left = True
        elif table_data[current_row][len(table_data[current_row])-1][1] != 1:
            left = True
        if current_row != 0:
            if table_data[current_row-1][current_column][1] != 1:
                top = True
        elif table_data[len(table_data)-1][current_column][1] != 1:
            top = True
        if current_row != len(table_data)-1:       
            if table_data[current_row+1][current_column][1] != 1:
                bottom = True
        elif table_data[0][current_column][1] !=1:
            bottom =True
    return [top, bottom, left, right]

def check_two_group(table_data, current_row, current_column):
    top, bottom, left, right = False, False, False, False
    answer = []
    if table_data[current_row][current_column][1] == 1:
        if current_column != len(table_data[current_row])-1:
            if table_data[current_row][current_column+1][1] == 1 and not check_one_group(table_data, current_row, current_column+1)[2]:
                right = True
                answer.append(table_data[current_row][current_column+1])
        elif table_data[current_row][0][1] == 1 and not check_one_group(table_data, current_row, 0)[2]:
            right = True
            answer.append(table_data[current_row][0])
        if current_column != 0:
            if table_data[current_row][current_column-1][1] == 1 and not check_one_group(table_data, current_row, current_column-1)[3]:
                left = True
                answer.append(table_data[current_row][current_column-1])
        elif table_data[current_row][len(table_data[current_row])-1][1] == 1 and not check_one_group(table_data, current_row, len(table_data[current_row])-1)[3]:
            left = True
            answer.append(table_data[current_row][len(table_data[current_row])-1])
        if current_row != 0:
            if table_data[current_row-1][current_column][1] == 1 and not check_one_group(table_data, current_row-1, current_column)[0]:
                top = True
                answer.append(table_data[current_row-1][current_column])
        elif table_data[len(table_data)-1][current_column][1] == 1 and not check_one_group(table_data, len(table_data)-1, current_column)[0]:
            top = True
            answer.append(table_data[len(table_data)-1][current_column])
        if current_row != len(table_data)-1:       
            if table_data[current_row+1][current_column][1] == 1 and not check_one_group(table_data, current_row+1, current_column)[1]:
                bottom = True
                answer.append(table_data[current_row+1][current_column])
        elif table_data[0][current_column][1] ==1 and not check_one_group(table_data, 0, current_column)[1]:
            bottom =True
            answer.append(table_data[0][current_column])
    return ([top, bottom, left, right], answer)