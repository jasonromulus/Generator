def histogram():
    print("hello")
    with open('villain.txt', 'r') as f:
        myList = f.read().split(" ")
        print(myList)
histogram()

# def load_script():
#     with open('villain.txt', 'r') as f:
#         read_data = f.read().split(" ")
#     f.closed
# print(read_data)
# load_script()