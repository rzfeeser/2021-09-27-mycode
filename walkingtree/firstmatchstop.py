#!/usr/bin/env python3
## Script to search and stop on first match
import os

## Define a function that stops searching on first match
def find(name, path):
    locations = []
    # start our loop
    for root, dirs, files in os.walk(path):
        if name in files:  # on a hit....
            locations.append(os.path.join(root, name))  # write into our list
    return locations


def main():

    lookfor = input("What am I looking for? ")
    lookwhere = input("What is the path in which I should search? ")

    print(find(lookfor, lookwhere))



if __name__ == "__main__":
    main()
