'''
Fully implemented
'''
import textwrap
from builtins import print as builtinprint


def println(string=''):
    builtinprint(textwrap.fill(string, 80))

def print(string=''):
    builtinprint(textwrap.fill(string, 80), end='')

def print_in_box(string, heavy):
    '''
    Prints a string inside of a box using box drawing characters. Passing None
    or '' will result in a return without any box being printed.
    '''
    if string != '' and string is not None:
        # FIXME don't have problems when the string is too long
        if(heavy):
            # top line of box index 1 to allow the different first character
            print('┏')
            for char in string:
                print('━')
            println('┓')

            # middle line of box
            println('┃' + string + '┃')

            # bottom line of box index 1 to allow the different first character
            print('┗')
            for char in string:
                print('━')
            println('┛')
        else:
            # top line of box index 1 to allow the different first character
            print('┌')
            for char in string:
                print('─')
            println('┐')

            # middle line of box
            println('│' + string + '│')

            # bottom line of box index 1 to allow the different first character
            print('└')
            for char in string:
                print('─')
            println('┘')

def prompt():
    println()
    println('What would you like to do?')
    string = input(':')
    return string
