#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Learning about conditionals - if, elif, else"""


def main():

    # create a simple string
    videogames = "Super Mario Bros"

    # is the "first letter of the string" an "S"
    if videogames[0] == "S":
        print("The first letter is the letter S!")

    if videogames[-1] != ".":
        print("You really should put a '.' at the end of Bros")

    vglist = videogames.split() # returns list from a string. SPLITs along a whitespace

    print(vglist)

    # test the very last word in our list
    if vglist[-1] == "Bros":
        print("Bros should have a '.' at the end of it")
        print("You can have multiple lines as well")
    elif vglist[-1] == "Bros.":
        print("Your abbreviation is correct!")
    else:
        print("I have no idea what the last word in your list is...")


print("Thanks for running the program!")

# call main
main()
