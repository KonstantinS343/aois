from copy import deepcopy

def glue_implicants(formula):
    if ')+(' in formula:
        form_of_formula = 'pdnf'
    else:
        form_of_formula = 'pcnf'
    tempalte_for_delete = ['(',')','+', '*']
    formula_without_extra_characters = [[]]
    formula = [i*(not(i == ')+(' or i == ')*(')) or ' ' for i in formula.split() if i not in tempalte_for_delete]
    index_of_space = 0
    
    for i in formula:
        if i == ' ':
            formula_without_extra_characters.append([])
            index_of_space+=1
        else:
            formula_without_extra_characters[index_of_space].append(i)
    #print(formula_without_extra_characters)
    return connect_two_implicats(formula_without_extra_characters, form_of_formula)

def calaculation_method(formula):
    formula_after_glue, base_formula, form_of_formula = glue_implicants(formula)
    return remove_extra_implications(formula_after_glue, form_of_formula)
    

def connect_two_implicats(formula, form_of_formula):
    formula_after_glue = []
    amount_equels_arguments = 0
    for i in range(0, len(formula)-1):
        for k in range(i+1, len(formula)):
            for j in range(0, len(formula[i])):
                if formula[i][j] == formula[k][j]:
                    amount_equels_arguments+=1
            if amount_equels_arguments == len(formula[0])-1:
                formula_after_glue.append(connect_arguments(formula[i], formula[k]))
            amount_equels_arguments = 0
    #print(formula_after_glue)
    #print(remove_extra_implications(formula_after_glue))
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
    for i in range(len(formula)):
        temp_formula = deepcopy(formula)
        if form_of_formula == 'pdnf':
            temp_formula, values_of_arguments = replace_arguments_on_0_1_pdnf(temp_formula, i, formula) 
        else:
            temp_formula, values_of_arguments = replace_arguments_on_0_1_pcnf(temp_formula, i, formula)  
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
        if i[0] != '!' and '!'+i in temp_cut_back_formula:
            temp_cut_back_formula.remove(i)
            temp_cut_back_formula.remove('!'+i)
            temp_expression = '1'
    for i in temp_cut_back_formula:
        temp_expression = logic_or(i, temp_expression) 
       
    if temp_expression == '1':
        return True
    return False

def check_on_extra_implicants_pcnf(cut_back_formula):
    for i in cut_back_formula:
        if i[0] != '!' and '!'+ i in cut_back_formula:
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
            return formula_after_open_staples
    else:
        if check_on_extra_implicants_pcnf(formula_after_open_staples):
            return []
        else:
            return formula_after_open_staples
    
                  
def translate_in_pcnf(formula):
    output_fomula = []
    for i in formula:
        implicat = f'({" + ".join(i)})*'
        output_fomula.append(implicat)
    print(''.join(output_fomula)[:-1])
    
def translate_in_pdnf(formula):
    output_fomula = []
    for i in formula:
        implicat = f'({" * ".join(i)})+'
        output_fomula.append(implicat)
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