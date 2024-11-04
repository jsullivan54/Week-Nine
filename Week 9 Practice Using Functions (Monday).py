def main():
    value = 99
    print (f'The value is currently: {value}')
    change_me(value)
    print (f'Value back in main after change_me is {value}')

def change_me(arg):
    print (f'I am changing the value.')
    arg = 0
    print (f'The changed value is {arg}')

main()