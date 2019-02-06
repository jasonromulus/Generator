import random
import sys

def load_script():

    f = open('/usr/share/dict/words', 'r')
    content = f.read().splitlines()
    f.close()
    return content

def command_line_input():

    return sys.argument[1:]

def random_generator():

    content = load_script()
    argument_input = command_line_input()
    arg_int = int(' '.join(argument_input))

def create_sentence():