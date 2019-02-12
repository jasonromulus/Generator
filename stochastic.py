import random

# This is my smaple line of text.
sentence = "one fish two fish red fish blue fish"
sentence_sample = sentence.split()

def histogram(sentence_sample):
    '''
    Returns unique values and the
    number of occurances of each
    '''
    # Here I am calling the dictonary in an array.
    dict = {}
    for word in sentence_sample:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    return(dict)

def list_of_list(dictionary):
    empty_list = []
    for words in dictionary:
        thing = [words, dictionary[words]]
        empty_list.append(thing)
    return(empty_list)

