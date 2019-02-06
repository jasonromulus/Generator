def histogram():
    print("hello")
    with open('villain.txt', 'r') as f:
        myList = f.read().split(" ")
        print(myList)
histogram()