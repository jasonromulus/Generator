import random
import sys

def load_dictonary():

    f = open('/usr/share/dict/words', 'r')
    content = f.read().splitlines()
    f.close()
    return content

def command_line_input():

    return sys.argument[1:]

def random_generator():

    content = load_dictonary()
    argument_input = command_line_input()
    argument_int = int(' '.join(argument_input))
    return random.choices(content, argument_int)

def create_sentence():
    results = ' '.join(random_generator())
    return results

print(create_sentence)

if __name__ == '__main__':
    create_sentence()