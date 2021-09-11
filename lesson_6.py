#### File: opening a file, reading from it, writing into it, closing it,
####       and various file methods that you should be aware of.

### function

### function defination: a block of code to implement some functionality

#A parameter: listed inside the parentheses in the function definition.
#An argument: value that is sent to the function when it is called.
import lesson_5

def my_func(param):
    print(param)

def my_func2(param1, param2):
    print(param1)
    print(param2)

def my_func3(*param):
    print(param[0])
    print(param[1])

### any order you want, you can use =
def my_func_4(param1, param2, param3):
    print(param1)
    print(param2)
    print(param3) \

### **kwargs
def my_func_5(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    #myFun(first='Geeks', mid='for', last='Geeks')

### default param
def my_func_6(name = "Tom"):
    print(name)

### pass do nothing:
def my_func_6(x):
    if (x < 10):
        pass
    else:
        print(x)

### recursion function
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


### practice leetcode 66

### import
### form .. import ...
### form .. import *










#import lesson_5
#from lesson_5 import my_file_write, my_file_read
from lesson_5 import *

if __name__ == '__main__':
    my_func("hello world")
    my_file_write()
    my_file_read()

