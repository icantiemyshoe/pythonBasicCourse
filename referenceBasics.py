# These are the three different ways you can reference objects using python

# Single Value
naked_ol_value = 'use me for everything'

# Definition /Method Based
def my_definition():
    print('This is executing the my_definition method')

# Class / Object Based

class MyClass(object):
    def __init__(self):
        self.value = 'my value'

    def print_value(self):
        print(self.value)

# Using positional arguements
def positional_args(must_use):
    print(must_use)

# Using key word (kwarg) arguements
def kwarg_args(optional_value='Default value'):
    print(optional_value)