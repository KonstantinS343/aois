from random import choice
import typing
import copy

class AssociatMemory:
    def __init__(self) -> None:
        self.size = 16
        self.memory = [[choice([0, 1]) for i in range(self.size)] for j in range(self.size)]
        self.memory_diagonal = self.memory
        
    def print_normal_from(self) -> None:
        if self.memory_diagonal == self.memory:
            for i in self.memory:
                memory_row = ' '.join([str(j) for j in i])
                print(memory_row)
        else:
            memory = self.to_normal()
            for i in memory:
                memory_row = ' '.join([str(j) for j in i])
                print(memory_row)
        
    def f1(self, columns: typing.List[int]) -> str:
        first_word = self.read_word(columns[0])
        second_word = self.read_word(columns[1])
        new_word = []
        for i in range(self.size):
            new_word.append(first_word[i] and second_word[i])
        self.set_word(new_word, columns[2])
        return ' '.join([str(j) for j in new_word])
    
    def f3(self, columns: typing.List[int]) -> str:
        new_word = self.read_word(columns[0])
        return ' '.join([str(j) for j in new_word])
    
    def f12(self, columns: typing.List[int]) -> str:
        new_word = self.read_word(columns[0])
        new_word = list(map(lambda x: 0 if x==1 else 1, new_word))
        self.set_word(new_word, columns[0])
        return ' '.join([str(j) for j in new_word])
    
    def f14(self, columns: typing.List[int]) -> str:
        first_word = self.read_word(columns[0])
        second_word = self.read_word(columns[1])
        new_word = []
        for i in range(self.size):
            new_word.append(first_word[i] and second_word[i])
        new_word = list(map(lambda x: 0 if x==1 else 1, new_word))
        self.set_word(new_word, columns[2])
        return ' '.join([str(j) for j in new_word])
    
    def set_word(self, word: typing.List[int], column: int) -> None:
        self.rotate_memory()
        self.memory_diagonal[column] = word[self.size-column:] + word[:self.size-column]
        self.rotate_memory()
    
    def read_word(self, column: int) -> typing.List[int]:
        self.rotate_memory()
        word = self.memory_diagonal[column][column:] + self.memory_diagonal[column][:column]
        self.rotate_memory()
        return word
    
    def __str__(self) -> str:
        for i in self.memory_diagonal:
            memory_row = ' '.join([str(j) for j in i])
            print(memory_row)   
        return ''
    
    def rotate_memory(self) -> None:
        self.memory_diagonal = [[self.memory_diagonal[i][j] for i in range(self.size)] for j in range(self.size)]
    
    def convert_to_diagonal(self) -> None:
        self.rotate_memory()
        for i in range(self.size):
            self.memory_diagonal[i] = self.memory_diagonal[i][self.size-i:] + self.memory_diagonal[i][:self.size-i]
        self.rotate_memory()
        
    def compare_words(self, words: typing.List[int], flag: bool) -> typing.List[int]:
        for i in words:
            print(' '.join([str(j) for j in i]))
            word = i
            for j in words:
                if flag:
                    if self.comparison(word, j):
                        word = j
                else:
                    if not self.comparison(word, j):
                        word = j
        return word
    
    def search(self, word: typing.List[int]) -> str:
        memory = self.to_normal()
        memory = [[memory[i][j] for i in range(self.size)] for j in range(self.size)]
        print(f'Input word: {word}')
        print('\n')
        less_then_input_word = []
        more_then_input_word = []

        for i in memory:
            if self.comparison(word, i):
                more_then_input_word.append(i)
            else:
                less_then_input_word.append(i)

        print('The words, that less then input word')
        biggest_word = self.compare_words(less_then_input_word, True)
        print('\n\n')
        print('The words, that more then input word')
        smallest_word = self.compare_words(more_then_input_word, False)
        print('Result: ')
        return ' '.join([str(i) for i in biggest_word]) + '\n' + ' '.join([str(i) for i in smallest_word])
    
    def comparison(self, first_word: typing.List[int], second_word: typing.List[int]) -> bool:
        g_variable, l_variable = 0, 0
        previous_g_variable, previous_l_variable = 0, 0
        
        for i in range(len(first_word)):
            g_variable = previous_g_variable or (not first_word[i] and second_word[i] and not previous_l_variable)
            l_variable = previous_l_variable or (first_word[i] and not second_word[i] and not previous_g_variable)
            previous_g_variable, previous_l_variable = g_variable, l_variable
            
        return g_variable
    
    def to_normal(self) -> typing.List[int]:
        normal_form = []
        self.rotate_memory()
        matrix = copy.deepcopy(self.memory_diagonal)
        self.rotate_memory()
        for i in range(len(matrix)):
            normal_form.append(self.read_word(i))
        return [[normal_form[i][j] for i in range(self.size)] for j in range(self.size)]
    
    def arimetic_operation(self, mask: typing.List[int]) -> None:
        memory = self.to_normal()
        memory = [[memory[i][j] for i in range(self.size)] for j in range(self.size)]
        pass_validation_by_mask = list(filter(lambda x: x[:3] == mask, memory))
        print(f'Mask: {"".join(str(i) for i in mask)}')
        print('Words that pass validation: ')
        new_words = []
        for i in pass_validation_by_mask:
            memory_row = ' '.join(str(j) for j in i)
            print(f'{memory_row}, index - {memory.index(i)}')
            new_words.append((memory.index(i), self.addiction(i)))
        
        print('Words after arifmetic operation: ')
        for i in new_words:
            memory_row = ' '.join(str(j) for j in i[1])
            print(memory_row)
            self.set_word(i[1], i[0])
    
    def addiction(self, word: typing.List[int]) -> typing.List[int]:
        A = word[3:7]
        B = word[7:11]
        S, dop_bit=[], 0
        for j in range(1, 5):
            S.append(A[-j]+B[-j]+dop_bit)
            if S[-1] == 3:
                S[-1] = 1
                dop_bit = 1
            elif S[-1] == 2:
                S[-1] = 0
                dop_bit = 1
            elif S[-1] == 1:
                S[-1] = 1
                dop_bit = 0
            else:
                S[-1] = 0
        S.append(dop_bit)
        S = list(reversed(S))
        return word[:11] + S
