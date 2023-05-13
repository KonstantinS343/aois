from memory import Memory

def main():
    memory = Memory([3, 67, 12, 33, 0, 1, 2, 23])
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
                print('\nFind by mask: 0xx0xxx1')
                memory.search_by_mask('0xx0xxx1')
                print(f'\nFind by mask: {mask}')
                memory.search_by_mask(mask)
            case _:
                break

if __name__=='__main__':
    main()