source_text = "one fish two fish red fish blue fish"

# Got help from Jackson Ho
def histogram_tuple(source_text):
    # create tuple list
    histogram_tuple = []

    for word in source_text:
        found = False
        # loops through my tuple
        for index, value in enumerate(histogram_tuple):
            # this checks if tuple and word match
            if value[0] == word:
                num = value[1] + 1
                found = True
                # this takes out the tuple
                histogram_tuple.pop(index)
                # this takes new word and appends it to the list
                histogram_tuple.append((word, num))
                break
        # this is for if the word is not found
        if not found:
            histogram_tuple.append((word, 1))

if __name__ == '__main__':
    histogram_tuple(source_text)