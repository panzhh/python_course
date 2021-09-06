# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#### dict: A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

def my_dict_test():
    # empty dictionary
    my_dict = {}

    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}

    # using dict()
    my_dict = dict({1: 'apple', 2: 'ball'})

    # from sequence having each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])
    # get vs [] for retrieving elements
    my_dict = {'name': 'Jack', 'age': 26}

    # Output: Jack
    print(my_dict['name'])

    # Output: 26
    print(my_dict.get('age'))

    # Trying to access keys which doesn't exist throws error
    # Output None
    print(my_dict.get('address'))

    # KeyError
    print(my_dict['address'])

    # Changing and adding Dictionary Elements
    my_dict = {'name': 'Jack', 'age': 26}

    # update value
    my_dict['age'] = 27

    # Output: {'age': 27, 'name': 'Jack'}
    print(my_dict)

    # add item
    my_dict['address'] = 'Downtown'

    # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    print(my_dict)

    # Removing elements from a dictionary

    # create a dictionary
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # remove a particular item, returns its value
    # Output: 16
    print(squares.pop(4))

    # Output: {1: 1, 2: 4, 3: 9, 5: 25}
    print(squares)

    # remove an arbitrary item, return (key,value)
    # Output: (5, 25)
    print(squares.popitem())

    # Output: {1: 1, 2: 4, 3: 9}
    print(squares)

    # remove all items
    squares.clear()

    # Output: {}
    print(squares)

    # delete the dictionary itself
    del squares

    # Throws Error
    print(squares)
    # Membership Test for Dictionary Keys
    squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

    # Output: True
    print(1 in squares)

    # Output: True
    print(2 not in squares)

    # membership tests for key only not value
    # Output: False
    print(49 in squares)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_dict_test()

