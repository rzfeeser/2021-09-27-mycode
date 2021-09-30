#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com
   
   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/
   
   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

#from mtgsdk import Card

import mtgsdk

# Get all cards
#cards = mtgsdk.Card.all()
#print(cards)

def main():


    card = mtgsdk.Card.find(386616)
    print(dir(card))
    print(card.name)   # print(card.name())


if __name__ == "__main__":
    main()

