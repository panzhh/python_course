#### File: opening a file, reading from it, writing into it, closing it,
####       and various file methods that you should be aware of.

### read(), readline(), readlines()
def my_file__read():
    f = open("sample.txt", "r")
    print(f.read())
    f.close()

    print()
    print("second method\n")
    print()

    with open("sample.txt", "r") as f:
        for line in f:
            print(line)

def my_file_write():
    f = open("sample.txt", "a")
    f.write("\nNow the file has more content!")
    f.close()

    # open and read the file after the appending:
    f = open("sample.txt", "r")
    print(f.read())


if __name__ == '__main__':
    my_file__read()
    my_file_write()

