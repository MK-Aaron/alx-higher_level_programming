#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    j = 0
    counter = -1

    for i in sys.argv:
        counter += 1
    if counter == 0:
        print("0 arguments") 
    elif counter == 1:
        print("{} argument:".format(counter, end=""))
        print("{}: {}".format(counter, i))
    elif counter > 1:
        print("{} arguments:".format(counter, end=""))
        for j in range (1, len(sys.argv)):
            print("{}: {}".format(j, sys.argv[j]))
