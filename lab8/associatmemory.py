from random import choice
import typing

class AssociatMemory:
    def __init__(self) -> None:
        self.size = 16
        #self.memory = [[choice([0, 1]) for i in range(self.size)] for j in range(self.size)]
        self.memory = [[0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
                        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
                        [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                        [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                        [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
                        [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                        [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                        [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
                        [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
                        [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1]]
        self.memory_diagonal = self.memory
        
    def f1(self, first_column, second_column, third_column):
        self.rotate_memory()
        first_word = self.memory_diagonal[first_column][first_column:] + self.memory_diagonal[first_column][:first_column]
        second_word = self.memory_diagonal[second_column][second_column:] + self.memory_diagonal[second_column][:second_column]
        res = []
        for i in range(self.size):
            res.append(first_word[i] and second_word[i])
        self.memory_diagonal[third_column] = res
        self.rotate_memory()
    
    def f3():
        pass
    
    def f12():
        pass
    
    def f14():
        pass
    
    def __str__(self) -> None:
        print('The usual matrix: ')
        for i in self.memory:
            print(i)
        if self.memory_diagonal != self.memory:
            print('The diagonal matrix: ')
            for i in self.memory_diagonal:
                print(i)
        return ''
            
    def read_from_memory(self, index) -> typing.List[int]:
        return [self.memory[i][index] for i in range(self.size)]
    
    def rotate_memory(self):
        self.memory_diagonal = [[self.memory_diagonal[i][j] for i in range(self.size)] for j in range(self.size)]
    
    def convert_to_diagonal(self):
        self.rotate_memory()
        for i in range(self.size):
            self.memory_diagonal[i] = self.memory_diagonal[i][self.size-i:] + self.memory_diagonal[i][:self.size-i]
        self.rotate_memory()
        
    def search(self):
        pass
    
    def addiction(self, mask):
        pass_validation_by_mask = list(filter(lambda x: x[:3] == mask, self.memory_diagonal))
        for i in pass_validation_by_mask:
            for j in range(4):
                i[11+j:] = i[3+j:] + i[7+j:]
    

def main():
    assm = AssociatMemory()
    assm.convert_to_diagonal()
    print(assm)
    assm.f1(4, 7, 2)

main()
    
    