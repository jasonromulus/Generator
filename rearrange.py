import random
import sys

def rearrange(list):
    print('list:', list)
    # this makes a new list
    new_list = []
    counter = len(list)
    while counter > 0:
        # this looks at the range and chooses a random index in the range
        random_index = random.randrange(len(list))
        # this deletes the chosen word from the list
        chosen_word = list.pop(random_index)
        print('word:', chosen_word)
        # this puts the chosen word in a new list
        new_list.append(chosen_word)
        counter -= 1
    # print('new_list:', new_list)
    # This prints out my new list and joins them so it looks proper with spaces
    results = " ".join(new_list)
    print(results)

if __name__ == '__main__':
    # words = ['apple', 'orange', 'banana']
    # rearrange(words)

    arguments = sys.argv[1:]
    rearrange(arguments)
