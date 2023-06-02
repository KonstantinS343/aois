from associatmemory import AssociatMemory


def main():
    memory = AssociatMemory()
    print('Memory in normal form: ')
    memory.print_normal_from()
    print('\n\n\n')
    
    memory.convert_to_diagonal()
    
    print('Memory in diagonal form: ')
    print(memory)
    print('\n\n\n')
    
    user_input = int(input('Take word by index: '))
    print(' '.join([str(i) for i in memory.read_word(user_input)]))
    print('\n\n\n')
    
    print('Function: ')
    print(f'The function 1 for 1, 2 and 3 words: {memory.f1([1, 2, 3])}')
    print(f'The function 3 for 1 word: {memory.f3([1, 2])}')
    print(f'The function 12 for 4 word: {memory.f12([4, 2])}')
    print(f'The function 14 for 1, 2 and 5 words: {memory.f14([1, 2, 5])}')
    print('\n\n\n')
    
    print('Memory in diagonal form: ')
    print(memory)
    print('\n\n')
    print('Memory in normal form: ')
    memory.print_normal_from()
    print('\n\n\n')
    
    print('Arifmetic operation: ')
    memory.arimetic_operation([0, 0, 1])
    print('\n')
    
    print('Memory in diagonal form: ')
    print(memory)
    print('\n\n')
    print('Memory in normal form: ')
    memory.print_normal_from()
    print('\n\n\n')
    
    print('Search: ')
    print(memory.search([0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0 ,0]))
    
    
    
if __name__ == '__main__':
    main()