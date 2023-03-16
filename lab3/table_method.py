from prettytable import PrettyTable

def table_method(formula, base_formula,form_of_formula, amout_values):
    create_table(amout_values, formula)
    
def create_table(amount_values, formula):
    amount_rows = len(amount_values)%2
    amount_columns = len(amount_values) - amount_rows
    table = PrettyTable()
    create_rows(amount_rows)
    create_columns(amount_columns)
    table.field_names = [f'{"".join(amount_values[:amount_rows])}/{"".join(amount_values[amount_columns-1:])}',
                         ]

def create_rows(amount_rows):
    rows = []
    for i in range(2 ** amount_rows):
        row = []
        for j in range(amount_rows):
            row.append((i >> j) & 1)
        rows.append(row)

def create_columns(amount_columns):
    columns = []
    for i in range(2 ** amount_columns):
        column = []
        for j in range(amount_columns):
            column.append((i >> j) & 1)
        columns.append(column)

