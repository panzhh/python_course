# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#### SET: unordered, unique (no duplicates) and must be immutable (cannot be changed).

def my_set_test():
    # Different types of sets in Python # set of integers
    my_set = {1, 2, 3}
    print(my_set)

    # set of mixed datatypes my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)

    # set cannot have duplicates # Output: {1, 2, 3, 4}
    my_set = {1, 2, 3, 4, 3, 2}
    print(my_set)

    # we can make set from a list # Output: {1, 2, 3}
    my_set = set([1, 2, 3, 2])
    print(my_set)

    # set cannot have mutable items # here [3, 4] is a mutable list # this will cause an error.
    #my_set = {1, 2, [3, 4]}

    # Distinguish set and dictionary while creating empty set
    # initialize a with {}
    a = {}

    # check data type of a
    print(type(a))

    # initialize a with set()
    a = set()

    # check data type of a
    print(type(a))

    # initialize my_set
    my_set = {1, 3}
    print(my_set)

    # set is unordered, can not use indexing and slicing.
    # my_set[0]
    # if you uncomment the above line
    # you will get an error
    # TypeError: 'set' object does not support indexing

    # add an element
    # Output: {1, 2, 3}
    my_set.add(2)
    print(my_set)

    # add multiple elements
    # Output: {1, 2, 3, 4}
    my_set.update([2, 3, 4])
    print(my_set)

    # add list and set
    # Output: {1, 2, 3, 4, 5, 6, 8}
    my_set.update([4, 5], {1, 6, 8})
    print(my_set)

    ### remove() and discrad().
    ''''
        The only difference between the two is that the discard() function leaves a
        set unchanged if the element is not present in the set.On the other hand, the
        remove() function will raise an error in such a condition( if element is not present in the
        set).
    '''
    # Difference between discard() and remove()

    # initialize my_set
    my_set = {1, 3, 4, 5, 6}
    print(my_set)

    # discard an element # Output: {1, 3, 5, 6}
    my_set.discard(4)
    print(my_set)

    # remove an element # Output: {1, 3, 5}
    my_set.remove(6)
    print(my_set)

    # discard an element # not present in my_set
    # Output: {1, 3, 5}
    my_set.discard(2)
    print(my_set)

    # remove an element # not present in my_set # you will get an error.
    # Output: KeyError
    #my_set.remove(2)

    ### pop(): is unordered, so totoally random results.
    # initialize my_set
    # Output: set of unique elements
    my_set = set("HelloWorld")
    print(my_set)

    # pop an element
    # Output: random element
    print(my_set.pop())

    # pop another element my_set.pop()
    print(my_set)

    # clear my_set
    # Output: set()
    my_set.clear()
    print(my_set)


    # set operation.
    # union,
    # Set union method
    # initialize A and B
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use | operator
    # Output: {1, 2, 3, 4, 5, 6, 7, 8}
    print(A | B)
    print(A.union(B))

    # Intersection of sets
    # initialize A and B
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # use & operator
    # Output: {4, 5}
    print(A & B)
    print (A.intersection(B))


    # in operator
    my_set = {"apple", "book", 'milk'}
    my_set2 = {"boy", "book", 'man'}
    for x in my_set:
        if x in my_set2:
            print(x)

    '''
    Built - in functions like:
    all(), any(), enumerate(), len(), max(), min(), sorted(), sum()
    etc.are commonly used with sets to perform different tasks.
    '''
    # enumerate function
    l1 = ["eat", "sleep", "repeat"]
    s1 = "geek"

    # creating enumerate objects
    obj1 = enumerate(l1)
    obj2 = enumerate(s1)

    print("Return type:", type(obj1))
    print(list(enumerate(l1)))

    # changing start index to 2 from 0
    print(list(enumerate(s1, 2)))


### exercise: remove dupicated elements from a list
def remove_duplicates_from_list(l):
    return l






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_set_test()
