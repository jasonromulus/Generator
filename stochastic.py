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

# This is my probability function
def stochastic(empty_list):
    word_frequency = 0
    probability = 0.0

    for item in empty_list:
        word_frequency += item[1]
    # random.uniform give a random number in the range
    random.uniform(0, 1)
    for value in sentence_sample:
        probability += value[1]/word_frequency