from typing import List
from prettytable import PrettyTable
from copy import deepcopy

class HashTable_element:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class Hash:

    def __init__(self) -> None:
        self.table_size = 16
        self.hash_function_const = 127
        self.hash_table: List[List[HashTable_element]] = [[] for _ in range(self.table_size)]

    def hash_function(self, input):
        element_key_value = HashTable_element(input[0], input[1])
        broken_word = [i for i in element_key_value.key]
        calculated_hash = ord(broken_word[0])*self.hash_function_const
        if len(broken_word) > 1:
            calculated_hash += ord(broken_word[1])
        if len(broken_word) > 2:
            for i in map(ord, broken_word[2:]):
                calculated_hash *= self.hash_function_const
                calculated_hash += i
        calculated_hash %= self.table_size
        return (calculated_hash, element_key_value)

    def add_new_hash_line(self, input):
        hash_index, key_value = self.hash_function(input)
        for i in range(len(self.hash_table[hash_index])):
            if self.hash_table[hash_index][i].key == key_value.key:
                self.hash_table[hash_index][i].value = key_value.value
                break
        else:
            self.hash_table[hash_index].append(key_value)

        if self.take_overflow():
            print(self.show_table())
            self.show_table_version_2()
            print('REBUILD TABLE')
            self.rebuild_table()

    def show_table(self):
        table_output_model = PrettyTable(['ID', 'KEY', 'VALUE'])
        for i in range(len(self.hash_table)):
            for j in range(0, len(self.hash_table[i])):
                table_output_model.add_row([i, self.hash_table[i][j].key, self.hash_table[i][j].value])
            if len(self.hash_table[i]) == 0:
                table_output_model.add_row([i, ' ', '  '])
        return table_output_model

    def show_table_version_2(self):
        for i in range(len(self.hash_table)):
            print(f'[{i}]', end=' : ')
            for j in range(0, len(self.hash_table[i])):
                if j != len(self.hash_table[i]) - 1:
                    print(f'{self.hash_table[i][j].key}:{self.hash_table[i][j].value}', end=' -> ')
                else:
                    print(f'{self.hash_table[i][j].key}:{self.hash_table[i][j].value}', end=' ')
            print('\n')

    def take_overflow(self):
        for i in self.hash_table:
            if not i:
                return False
        return True

    def delete_element(self, input):
        hash_key, elements = self.hash_function([input, ''])
        for i in self.hash_table[hash_key]:
            if i.key == input:
                self.hash_table[hash_key].remove(i)

    def search(self, key):
        hash_key, _ = self.hash_function([key, ''])
        for i in self.hash_table[hash_key]:
            if i.key == key:
                print(i.value)
                break
        else:
            raise Exception('Key error')

    def rebuild_table(self):
        temp_hash_table = deepcopy(self.hash_table)
        self.table_size *= 2
        self.hash_table: List[List[HashTable_element]] = [[] for _ in range(self.table_size)]

        for i in temp_hash_table:
            for j in i:
                self.add_new_hash_line([j.key, j.value])
