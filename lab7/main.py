from memory import Memory

def main():
    memory = Memory([3, 67, 12, 33, 0, 1, 2, 23])
    memory()
    print('\nSort in ascending order:')
    memory.sort(False)
    memory()
    print('\nSort in descending order:')
    memory.sort(True)
    memory()

if __name__=='__main__':
    main()