#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 arguments.") 
    elif counter == 1:
        print("{} argument:".format(counter))
    else:
        print("{} arguments:".format(counter))
    for j in range(1, len(sys.argv)):
            print("{}: {}".format(j, sys.argv[j]))
