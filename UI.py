'''
Fully implemented
'''
import textwrap
from builtins import print as builtinprint

def println(string=''):
    '''
    Print string, wrapped at 80 chars. Adds a newline to the end of the string.
    Use instead of print() to ensure wrapping works as intended.
    '''
    builtinprint(textwrap.fill(string, 80))

def print(string=''):
    '''
    Print string, wrapped at 80 chars. Does not add a newline to the end of the
    string. You probably want UI.println().
    '''
    builtinprint(textwrap.fill(string, 80), end='')

class StringTooLongException(Exception):
    '''
    This exception should be raised when a string is too long for some reason
    (eg box-drawing). It should not be raised in normal usage.
    '''

def wrap_in_box(string, heavy):
    '''
    Returns a string inside of a box using box drawing characters. Passing None
    or '' will result in a return of '', with no box. There is a newline at the
    end, leaving the string on the line following bottom of the box.
    '''
    if len(string) > 78:
        raise StringTooLongException(string)
    return_string = ''
    if string != '' and string is not None:
        if(heavy):
            # top line of box index 1 to allow the different first character
            return_string += '┏'
            for char in string:
                return_string += '━'
            return_string += '┓\n'

            # middle line of box
            return_string += '┃' + string + '┃\n'

            # bottom line of box index 1 to allow the different first character
            return_string += '┗'
            for char in string:
                return_string += '━'
            return_string += '┛\n'
        else:
            # top line of box index 1 to allow the different first character
            return_string += '┌'
            for char in string:
                return_string += '─'
            return_string += '┐\n'

            # middle line of box
            return_string += '│' + string + '│\n'

            # bottom line of box index 1 to allow the different first character
            return_string += '└'
            for char in string:
                return_string += '─'
            return_string += '┘\n'
    return return_string

def print_in_box(string, heavy):
    '''
    DEPRECATED: Use UI.wrap_in_box() instead, then call UI.println(). Prints a
    string inside of a box using box drawing characters.  Passing None or ''
    will result in a return without any box being printed.
    '''
    if len(string) > 78:
        raise StringTooLongException(string)
    if string != '' and string is not None:
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
