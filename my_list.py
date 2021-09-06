# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



### list usage
### list define, index,
#How to create a list?

#Access List Elements
#Negative indexing
#How to slice lists in Python?
#Add/Change List Elements
#append/extend
#remove/delte/clear
#pop
#Python List Methods
#append() - Add an element to the end of the list
#extend() - Add all elements of a list to the another list
#insert() - Insert an item at the defined index
#remove() - Removes an item from the list
#pop() - Removes and returns an element at the given index
#clear() - Removes all items from the list
#index() - Returns the index of the first matched item
#count() - Returns the count of the number of items passed as an argument
#sort() - Sort items in a list in ascending order
#reverse() - Reverse the order of items in the list
#copy() - Returns a shallow copy of the list


#1. Filtering Lists with Python
    #original_list = [1,2,3,4,5]
    #
    #def filter_three(number):
    #  return number > 3
    #
    #filtered = filter(filter_three, original_list)
    #
    #filtered_list = list(filtered)
    #
    #print(filtered_list)
    ## Returns [4,5]

#2    With List Comprehensions
#    original_list = [1, 2, 3, 4, 5]
#
#    filtered_list = [number for number in original_list if number > 3]
#
#    print(filtered_list)
#
#    # Return [4,5]

# coding1 2sum questions
# coding2 most frequency words: 347Top K Frequent Elements

def listFunc():
    myList = [1, 2, 3, 4, 5, 6, 7]
    if len(myList) == 0:
        print("empty list")
    print(myList)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    listFunc()
