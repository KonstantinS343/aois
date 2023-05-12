class Memory:
    def __init__(self, inputs):
        self.memory = []
        
        for i in inputs:
            self.memory.append(self.translate_to_binary(i))
        
    def __call__(self):
        for i in self.memory:
            print(i)
    
    def translate_to_binary(self, decimal_number):
        binary_number = []
        while decimal_number:
            binary_number.append(decimal_number%2)
            decimal_number//=2
        
        for i in range(8 - len(binary_number)):
            binary_number.append(0)
        
        return list(reversed(binary_number))
    
    def translate_to_decimal(self):
        decimal_number = []
        temp_decimal_number = 0
        
        for i in self.memory:
            for j in range(len(i)):
                temp_decimal_number+=2**(len(i)-j-1)*i[j]
            decimal_number.append(temp_decimal_number)
            temp_decimal_number = 0
        return decimal_number
    
    def comparison(self, first_word, second_word, flag):
        g_variable, l_variable = 0, 0
        previous_g_variable, previous_l_variable = 0, 0
        
        for i in range(len(first_word)):
            g_variable = previous_g_variable or (not first_word[i] and second_word[i] and not previous_l_variable)
            l_variable = previous_l_variable or (first_word[i] and not second_word[i] and not previous_g_variable)
            previous_g_variable, previous_l_variable = g_variable, l_variable
            
        if g_variable:
            return flag
        elif l_variable:
            return not flag
    
    def sort(self, sort_flag):
        for i in range(len(self.memory)):
            for j in range(len(self.memory)-1-i):
                if self.comparison(self.memory[j], self.memory[j+1], sort_flag):
                    self.memory[j], self.memory[j+1] = self.memory[j+1], self.memory[j]
        print(str(self.translate_to_decimal())+'\n')        