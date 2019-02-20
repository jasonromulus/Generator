import random
import sys

def load_dictonary():
    # This is opening my computers dictonary to read it.
    f = open('/usr/share/dict/words', 'r')
    content = f.read().splitlines()
    f.close()
    return content

def command_line_input():
    # This is creating the arugment for my file.
    return sys.argv[1:]

def random_generator():
    # This is loading my dictonary.
    content = load_dictonary()
    # This is to give my argument input.
    argument_input = command_line_input()
    arg_int = int(' '.join(argument_input))
    # This will return a random choice based on content.
    return random.choices(content, k=arg_int)

def create_sentence():
    # This creates the sentences
    results = ' '.join(random_generator())
    return results

print(create_sentence)

if __name__ == '__main__':
    create_sentence()