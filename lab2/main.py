from logic import LogicFunction

def main():
    function = LogicFunction()
    function.handler_input_formula('!((x1+x3)*!(x2*x3))')
    function.create_logic_table()

if __name__ == '__main__':
    main()