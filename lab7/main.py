from memory import Memory
from random import randint

def main():
    input_list = []
    for i in range(8):
        input_list.append(randint(0, 100))
    memory = Memory(input_list)
    user_input = ' '
    memory()
    while user_input:
        user_input = input('1 - sort;\n2 - find;\n')
        match user_input:
            case '1':
                print('\nSort in ascending order:')
                memory.sort(False)
                memory()
                print('\nSort in descending order:')
                memory.sort(True)
                memory()
            case '2':
                mask = input('Enter mask(use "x" instead spaces): ')
                print(f'\nFind by mask: {mask}')
                memory.search_by_mask(mask)
            case _:
                break

if __name__=='__main__':
    main()