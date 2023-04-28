from copy import deepcopy


def glue_implicants(formula):
    if ')+(' in formula or ' * ' in formula:
        form_of_formula = 'pdnf'
    elif ')*(' in formula or ' + ' in formula:
        form_of_formula = 'pcnf'
    else:
        form_of_formula = ''
    tempalte_for_delete = ['(', ')', '+', '*']
    formula_without_extra_characters = [[]]
    formula = [i * (not (i == ')+(' or i == ')*('))
               or ' ' for i in formula.split() if i not in tempalte_for_delete]
    index_of_space = 0

    for i in formula:
        if i == ' ':
            formula_without_extra_characters.append([])
            index_of_space += 1
        else:
            formula_without_extra_characters[index_of_space].append(i)
    return connect_two_implicats(
        formula_without_extra_characters,
        form_of_formula)


def calaculation_method(formula):
    if len(formula) == 0:
        return '-'
    formula_after_glue, base_formula, form_of_formula = glue_implicants(formula)
    formula_after_glue_again = formula_after_glue
    while True:
        size = len(formula_after_glue_again)
        formula_after_glue_again, base_formula, form_of_formula = connect_two_implicats(
            formula_after_glue_again, form_of_formula)
        if len(formula_after_glue_again[0]) == 1:
            formula_in_list = set([j for i in formula_after_glue_again for j in i])
            formula_in_list = delete_extra_arguments(list(formula_in_list))
            return formula_in_list
        if size == len(formula_after_glue_again):
            break
        size_of_implicat = len(formula_after_glue_again[0])
        for i in formula_after_glue_again:
            if len(i) != size_of_implicat:
                temp_formula_after_glue_again = deepcopy(formula_after_glue_again)
                for i in temp_formula_after_glue_again:
                    if formula_after_glue_again.count(i) > 1:
                        formula_after_glue_again.remove(i)
                return remove_extra_implications(formula_after_glue_again, form_of_formula)
    return remove_extra_implications(formula_after_glue, form_of_formula)


def delete_extra_arguments(formula):
    temp_formula = deepcopy(formula)
    for i in formula:
        if i in temp_formula and '!' + i in temp_formula:
            temp_formula.remove(i)
            temp_formula.remove('!' + i)
    return [[i] for i in temp_formula]

def check_size(formula):
    if len(formula) > 0:
        size = len(formula[0])
    else:
        return False
    for i in formula:
        if len(i) != size:
            return False
    return True

def connect_two_implicats(formula, form_of_formula):
    formula_after_glue, differense, append_later, use_implicats = [], [], [], []
    if not check_size(formula) or len(formula) == 1:
        return  (formula, formula, form_of_formula)
    for i in range(0, len(formula) - 1):
        formula_size = len(formula_after_glue)
        for k in range(i + 1, len(formula)):
            for j in range(0, len(formula[i])):
                if formula[i][j] != formula[k][j]:
                    differense.append((formula[i][j], formula[k][j]))
            if len(differense) == 1 and differense[0][0][-1] == differense[0][1][-1]:
                formula_after_glue.append(
                    connect_arguments(formula[i], formula[k]))
                use_implicats.append(formula[k])
            differense.clear()
        if len(formula_after_glue) == formula_size and formula[i] not in use_implicats:
            append_later.append(formula[i])
    if len(formula_after_glue) == 0:
        return (formula, formula, form_of_formula)
    else:
        formula_after_glue = append_later + formula_after_glue + ([formula[-1]] \
            if formula[-1] not in use_implicats else [])
    return (formula_after_glue, formula, form_of_formula)


def connect_arguments(first_implicat, second_implicant):
    glued_arguments = []
    for i in range(len(first_implicat)):
        if first_implicat[i] == second_implicant[i]:
            glued_arguments.append(first_implicat[i])
    return glued_arguments


def replace_arguments_on_0_1_pdnf(temp_formula, current_implicat, formula):
    values_of_arguments = dict()
    for j in range(len(formula[current_implicat])):
        values_of_arguments[formula[current_implicat][j]] = '1'
        if temp_formula[current_implicat][j][0] == 'x':
            values_of_arguments['!' + formula[current_implicat][j]] = '0'
        else:
            values_of_arguments[formula[current_implicat][j][1:]] = '0'
        temp_formula[current_implicat][j] = '1'
    return (temp_formula, values_of_arguments)


def replace_arguments_on_0_1_pcnf(temp_formula, current_implicat, formula):
    values_of_arguments = dict()
    for j in range(len(formula[current_implicat])):
        values_of_arguments[formula[current_implicat][j]] = '0'
        if temp_formula[current_implicat][j][0] == 'x':
            values_of_arguments['!' + formula[current_implicat][j]] = '1'
        else:
            values_of_arguments[formula[current_implicat][j][1:]] = '1'
        temp_formula[current_implicat][j] = '0'
    return (temp_formula, values_of_arguments)


def remove_extra_implications(formula, form_of_formula):
    formula_after_removed_implicats = []
    if len(formula) == 1 or len(formula[0]) == 1:
        return formula
    for i in range(len(formula)):
        temp_formula = deepcopy(formula)
        if form_of_formula == 'pdnf':
            temp_formula, values_of_arguments = replace_arguments_on_0_1_pdnf(
                temp_formula, i, formula)
        else:
            temp_formula, values_of_arguments = replace_arguments_on_0_1_pcnf(
                temp_formula, i, formula)
        for j in range(len(temp_formula)):
            for k in range(len(temp_formula[j])):
                if temp_formula[j][k] in values_of_arguments:
                    temp_formula[j][k] = values_of_arguments[temp_formula[j][k]]
        if cut_back_arguments(temp_formula, form_of_formula):
            formula_after_removed_implicats.append(formula[i])
    return formula_after_removed_implicats


def check_on_extra_implicants_pdnf(cut_back_formula):
    temp_expression = ''
    temp_cut_back_formula = deepcopy(cut_back_formula)
    for i in cut_back_formula:
        if str(i).isdigit():
            continue
        if i[0] != '!' and '!' + i in temp_cut_back_formula:
            temp_cut_back_formula.remove(i)
            temp_cut_back_formula.remove('!' + i)
            temp_expression = '1'
    for i in temp_cut_back_formula:
        temp_expression = logic_or(i, temp_expression)

    if temp_expression == '1':
        return True
    return False


def check_on_extra_implicants_pcnf(cut_back_formula):
    for i in cut_back_formula:
        if i[0] != '!' and '!' + i in cut_back_formula:
            return True
    return False


def cut_back_arguments(temp_formula, form_of_formula):
    formula_after_open_staples = []
    for i in temp_formula:
        if ''.join(i).isdigit():
            continue
        expression_in_staples = i[0]
        for j in i[1:]:
            if form_of_formula == 'pdnf':
                expression_in_staples = logic_and(expression_in_staples, j)
            else:
                expression_in_staples = logic_or(expression_in_staples, j)
        formula_after_open_staples.append(expression_in_staples)
    if form_of_formula == 'pdnf':
        if check_on_extra_implicants_pdnf(formula_after_open_staples):
            return []
        else:
            return True
    else:
        if check_on_extra_implicants_pcnf(formula_after_open_staples):
            return []
        else:
            return True


def translate_in_pcnf(formula):
    output_fomula = []
    if isinstance(formula, str):
        print(formula)
        return
    elif len(formula) == 0:
        print(0)
        return
    if len(formula[0]) == 1:
        output_fomula.append('(')
    for i in formula:
        if len(i) == 1:
            implicat = f'{" + ".join(i)}*'
        else:
            implicat = f'({" + ".join(i)})*'
        output_fomula.append(implicat)
    if len(formula[0]) == 1:
        output_fomula[-1] = output_fomula[-1][:-1] + ')'
        print(''.join(output_fomula))
    else:
        print(''.join(output_fomula)[:-1])


def translate_in_pdnf(formula):
    output_fomula = []
    if isinstance(formula, str):
        print(formula)
        return
    elif len(formula) == 0:
        print(0)
        return
    if len(formula[0]) == 1:
        output_fomula.append('(')
    for i in formula:
        if len(i) == 1:
            implicat = f'{" * ".join(i)}+'
        else:
            implicat = f'({" * ".join(i)})+'
        output_fomula.append(implicat)
    if len(formula[0]) == 1:
        output_fomula[-1] = output_fomula[-1][:-1] + ')'
        print(''.join(output_fomula))
    else:
        print(''.join(output_fomula)[:-1])


def logic_and(first_argument, second_argument):
    if first_argument == second_argument:
        return first_argument
    if first_argument.isdigit() and second_argument.isdigit():
        return str(int(first_argument) and int(second_argument))
    if first_argument[0] == 'x' or first_argument[0] == '!':
        if second_argument == '1':
            return first_argument
        else:
            return '0'
    else:
        if first_argument == '1':
            return second_argument
        else:
            return '0'


def logic_or(first_argument, second_argument):
    if first_argument == second_argument:
        return first_argument
    if first_argument.isdigit() and second_argument.isdigit():
        return str(int(first_argument) or int(second_argument))
    if first_argument[0] == 'x' or first_argument[0] == '!':
        if second_argument == '1':
            return '1'
        else:
            return first_argument
    else:
        if first_argument == '1':
            return '1'
        else:
            return second_argument
