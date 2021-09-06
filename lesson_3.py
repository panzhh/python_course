# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#### TUPE: A tuple in Python is similar to a list, we cannot change the elements of a tuple

def my_tupe_test():
    # Different types of tuples

    # Empty tuple
    my_tuple = ()
    print(my_tuple)

    # Tuple having integers
    my_tuple = (1, 2, 3)
    print(my_tuple)

    # tuple with mixed datatypes
    my_tuple = (1, "Hello", 3.4)
    print(my_tuple)

    # nested tuple
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(my_tuple)

    # Accessing tuple elements using indexing
    my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

    print(my_tuple[0])  # 'p'
    print(my_tuple[5])  # 't'

    # IndexError: list index out of range
    # print(my_tuple[6])

    # Index must be an integer
    # TypeError: list indices must be integers, not float
    # my_tuple[2.0]

    # nested tuple
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

    # nested index
    print(n_tuple[0][3])  # 's'
    print(n_tuple[1][1])  # 4

    # Accessing tuple elements using slicing
    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

    # elements 2nd to 4th
    # Output: ('r', 'o', 'g')
    print(my_tuple[1:4])

    # elements beginning to 2nd
    # Output: ('p', 'r')
    print(my_tuple[:-7])

    # elements 8th to end
    # Output: ('i', 'z')
    print(my_tuple[7:])

    # elements beginning to end
    # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    print(my_tuple[:])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_tupe_test()

