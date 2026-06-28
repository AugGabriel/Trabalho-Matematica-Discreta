def preorder(directory):
    for elem in directory:
        if type(elem) == int:
            print(elem)
        else:
            preorder(elem)


simulation = [1, 2, 3, [4, 5, [6, 7, 8], 9, 10], 11, [12, 13]]
preorder(simulation)