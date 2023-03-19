from prettytable import PrettyTable
import math

def table_method(formula, base_formula,form_of_formula, amount_values, table_data):
    if not form_of_formula:
        print('Не существует!')
        return
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
        minimize_function(temp_table, form_of_formula)
    else:
        minimize_function(temp_table, form_of_formula)

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

def minimize_function(table_data, form_of_formula):
    if check_all_in_group(table_data, 1*(form_of_formula == 'pdnf')):
        print(table_data)
        return
    output = [[]]
    for i in range(0, len(table_data)):
        for j in range(0, len(table_data[i])):
            choose_group(check_four_group(table_data, i, j, 1*(form_of_formula == 'pdnf')), output ,table_data[i][j])
    output.append([]) 
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            if all(check_one_group(table_data, i, j, 1*(form_of_formula == 'pdnf'))):
                output[-1].append((table_data[i][j], ))          
    output.append([])
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            result = check_two_group(table_data, i, j, 1*(form_of_formula == 'pdnf'))
            choose_group(result, output, table_data[i][j])                  
    print(output)   

def choose_group(result, output, current_element):
    all_elements = [k for i in output for j in i for k in j]
    if len(result) == 0:
        return 
    if current_element not in all_elements or len(result[0]) == 4:
        for i in result:
            if (i not in all_elements and i not in output[-1]) or len(result) == 1:
                if type(result[0][0]) == tuple: 
                    output[-1].append(i)
                else:
                    output[-1].append((current_element, i))
def check_one_group(table_data, current_row, current_column, form_of_formula):
    top, bottom, left, right = False, False, False, False
    if table_data[current_row][current_column][1] == form_of_formula:
        if current_column != len(table_data[current_row])-1:
            if table_data[current_row][current_column+1][1] != form_of_formula:
                right = True
        elif table_data[current_row][0][1] != form_of_formula:
            right = True
        if current_column != 0:
            if table_data[current_row][current_column-1][1] != form_of_formula:
                left = True
        elif table_data[current_row][len(table_data[current_row])-1][1] != form_of_formula:
            left = True
        if current_row != 0:
            if table_data[current_row-1][current_column][1] != form_of_formula:
                top = True
        else:
            top = True
        if current_row != len(table_data)-1:       
            if table_data[current_row+1][current_column][1] != form_of_formula:
                bottom = True
        else:
            bottom = True
    return [top, bottom, left, right]

def check_two_group(table_data, current_row, current_column, form_of_formula):
    answer = []
    if table_data[current_row][current_column][1] == form_of_formula:
        if current_column != len(table_data[current_row])-1:
            if table_data[current_row][current_column+1][1] == form_of_formula:
                answer.append(table_data[current_row][current_column+1])
        elif table_data[current_row][0][1] == form_of_formula:
            answer.append(table_data[current_row][0])
        if current_column != 0:
            if table_data[current_row][current_column-1][1] == form_of_formula:
                answer.append(table_data[current_row][current_column-1])
        elif table_data[current_row][len(table_data[current_row])-1][1] == form_of_formula:
            answer.append(table_data[current_row][len(table_data[current_row])-1])
        if current_row != 0:
            if table_data[current_row-1][current_column][1] == form_of_formula:
                answer.append(table_data[current_row-1][current_column])
        if current_row != len(table_data)-1:       
            if table_data[current_row+1][current_column][1] == form_of_formula:
                answer.append(table_data[current_row+1][current_column])
    return answer

def check_four_group(table_data, current_row, current_column, form_of_formula):
    answer = []
    if table_data[current_row][current_column][1] == form_of_formula:
        if current_column == 0:
            temp = []
            for i in range(current_column, len(table_data[current_row])):
                if table_data[current_row][i][1] == form_of_formula:
                    temp.append(table_data[current_row][i])
                else:
                    break
            if table_data[current_row][0][1] == form_of_formula:
                for i in range(0, current_column):
                    if table_data[current_row][i][1] == form_of_formula:
                        temp.append(table_data[current_row][i])
                    else:
                        break
            if len(temp) == 4:
                answer.append(tuple(temp))
        if current_row == 0:
            if current_column != len(table_data[current_row])-1:
                if table_data[current_row][current_column+1][1] == form_of_formula and table_data[current_row+1][current_column][1] == form_of_formula and \
                    table_data[current_row+1][current_column+1][1] == form_of_formula:
                        answer.append((table_data[current_row][current_column], table_data[current_row][current_column+1], 
                                       table_data[current_row+1][current_column], table_data[current_row+1][current_column+1]))
            else:
                if table_data[current_row][0][1] == form_of_formula and table_data[current_row+1][current_column][1] == form_of_formula and \
                    table_data[current_row+1][0][1] == form_of_formula:
                        answer.append((table_data[current_row][current_column], table_data[current_row+1][current_column], 
                                       table_data[current_row][0], table_data[current_row+1][0]))
    return answer

def check_all_in_group(table_data, form_of_formula):
    for i in table_data:
        for j in i:
            if j[1] != form_of_formula:
                return False
    return True