#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of loops and working with files"""

## imports
# standard library imports go first

# 3rd party library imports go next

## classes

## functions

# our main function is the single function invoked
# when our program begins to run
# this is convention
def main():
    """called at runtime"""

    # our code and function calls go here

    ## open a txt file and read in data
    
    # old way to open / close a file (still works!)
    openfile = open("example.txt", "r")   # creates a file object named "openfile" in readmode
    
    # rather than read all lines into a list (i.e into memory), we can take it line by line
    for line in openfile:   # (line == single line from file)
        print(line.rstrip("\n"))         # this would print the entire line from our file        
        print(line.split()[0])           # line.split() returns a LIST containing each word SPLIT along a whitespace, we then select word [0]
    openfile.close()      # we MUST close our file because we opened it using the OLD method


    # new way to open / close a file
    with open("example.txt", "r") as openfile:
        for line in openfile:
            print(line.rstrip("\n"))
            print(line.split()[0])
    # no need to close anything
    # the close happens automatically when the indentation ends

    
    ## open a txt file and write out data (create / overwrite)
    with open("created.txt", "w") as openfile:
        for word in ["two", "terribly", "tired", "toads", "trotted", "along", "the", "road"]:    # this is just a list
            openfile.write(word + "...\n")  # each time through the loop, we add this to our file "created.txt"
            # print(word, file=openfile)  # this does the same thing as the line above

    
    ## open a txt file and write out data (append)
    with open("appending.txt", "a") as of:   # appending.txt will be created if it does not exist, and will be added to if it does
        for key in {"a": "you can also", "b": "loop across", "c": "dictionaries"}:   # this will grab the KEY from each key:value pair
            print(key, file=of)


# best practice way to call your code
# allows your code to be IMPORTED without being automatically
# exectued by the importer
if __name__ == "__main__":
    main()
