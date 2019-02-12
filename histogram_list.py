source_text = "one fish two fish red fish blue fish"

def histogram(source_text):
    # print("hello")
    # create a list
    text_list = []

    # goes through the source text
    for word in source_text:
        add_word = False
        for row in text_list:
            # checks if word is the same
            if word == row[0]:
                row[1] += 1
                add_word = True
                # this stops the loop from continuing
                break

        if add_word == False:
            text_list.append([word,1])

    # print(text_list)

if __name__ == '__main__':
    histogram(source_text)