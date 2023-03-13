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
    connect_two_implicats(formula_without_extra_characters)
    
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
    print(formula_after_glue)

def connect_arguments(first_implicat, second_implicant):
    glued_arguments = []
    for i in range(len(first_implicat)):
        if first_implicat[i] == second_implicant[i]:
            glued_arguments.append(first_implicat[i])
    return glued_arguments

def remove_extra_implications(formula):
    temp = []
    temp_formula = formula
    values = dict()
    