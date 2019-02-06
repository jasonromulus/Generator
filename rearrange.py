import random
import sys

def rearrange(list):
    print('list:', list)
    new_list = []
    counter = len(list)
    while counter > 0:
        random_index = random.randrange(len(list))
        chosen_word = list.pop(random_index)
        print('word:', chosen_word)
        new_list.append(chosen_word)
        counter -= 1
    print('new_list:', new_list)
    results = " ".join(new_list)
    print(results)

if __name__ == '__main__':
    # words = ['apple', 'orange', 'banana']
    # rearrange(words)

    arguments = sys.argv[1:]
    rearrange(arguments)
