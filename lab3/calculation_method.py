from copy import deepcopy

def glue_implicants(formula):
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
    return connect_two_implicats(formula_without_extra_characters)
    
def connect_two_implicats(formula):
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
    return remove_extra_implications(formula_after_glue)

def connect_arguments(first_implicat, second_implicant):
    glued_arguments = []
    for i in range(len(first_implicat)):
        if first_implicat[i] == second_implicant[i]:
            glued_arguments.append(first_implicat[i])
    return glued_arguments

def replace_arguments_on_0_1(temp_formula, current_implicat, formula):
    values_of_arguments = dict()
    for j in range(len(formula[current_implicat])):
        if temp_formula[current_implicat][j][0] == 'x':
            values_of_arguments[formula[current_implicat][j]] = '1'
            temp_formula[current_implicat][j] = '1'
            values_of_arguments['!' + formula[current_implicat][j]] = '0'
        else:
            values_of_arguments[formula[current_implicat][j]] = '1'
            temp_formula[current_implicat][j] = '1'
            values_of_arguments[formula[current_implicat][j][1:]] = '0'
    return (temp_formula, values_of_arguments)

def remove_extra_implications(formula):
    formula_after_removed_implicats = []
    for i in range(len(formula)):
        implicats_after_insert_0_and_1 = []
        temp_formula = deepcopy(formula) 
        temp_formula, values_of_arguments = replace_arguments_on_0_1(temp_formula, i, formula)   
        for j in range(len(temp_formula)):
            for k in range(len(temp_formula[j])):
                if temp_formula[j][k] in values_of_arguments:
                    temp_formula[j][k] = values_of_arguments[temp_formula[j][k]]
            if not ''.join(temp_formula[j]).isdigit():
                implicats_after_insert_0_and_1.append(temp_formula[j])
        if cut_back_arguments(implicats_after_insert_0_and_1):
            formula_after_removed_implicats.append(formula[i])
    return formula_after_removed_implicats
        
def check_on_extra_implicants(cut_back_formula):
    arguments = ['0']
    temp_cut_back_formula = deepcopy(cut_back_formula)
    for i in cut_back_formula:
        if i not in arguments and i[0] == 'x' and ('!'+i) not in temp_cut_back_formula and temp_cut_back_formula:
            arguments = []
            arguments.append(i)
        elif i[0] == 'x' and ('!'+i) in temp_cut_back_formula and i in temp_cut_back_formula:
            temp_cut_back_formula.remove(i)
            temp_cut_back_formula.remove('!'+i)
        if i not in arguments and i[0] == '!' and i[1:] not in temp_cut_back_formula and temp_cut_back_formula:
            arguments = []
            arguments.append(i)
        elif i[0] == '!' and i[1:] in temp_cut_back_formula and i in temp_cut_back_formula:
            temp_cut_back_formula.remove(i)
            temp_cut_back_formula.remove(i[1:])
            
    if ''.join(arguments).isdigit():
        return True
    return False
        
def cut_back_arguments(temp_formula):
    formula_after_open_staples = []
    expression_in_staples = 1
    for i in temp_formula:
        for j in i:
            try:
                number_in_int_form = int(j)
            except:
                expression_in_staples*=j
            else:
                expression_in_staples*=number_in_int_form
        if expression_in_staples:
            formula_after_open_staples.append(expression_in_staples)
        expression_in_staples = 1
    if check_on_extra_implicants(formula_after_open_staples):
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