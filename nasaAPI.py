#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   making an API request to NASA using best practice"""

import sys # quit if we encounter a non 200
import os  # grab our env variable

# python3 -m pip install requests
import requests  # make HTTP GET request

API = "https://api.nasa.gov/planetary/apod?"   # root API to lookup

KEYFILE = "/home/student/nasa.key"

def credget():
    """returns NASA creds to be used in API lookup"""
    # attempt to harvest an API key from an environmental variable (priority)
    # if we can't find one... try looking in KEYFILE for a API key...
    # if all else fails, use "DEMO_KEY"
    try:
        mykey = os.environ['NASAKEY']   # this will cause an ERROR (exception) if the key isn't set
    except:
        print(os.environ)
        if os.path.isfile(KEYFILE):   # is KEYFILE even a real file?
            with open(KEYFILE) as of:
                mykey = of.readline()
        else:
            mykey = "DEMO_KEY"  # this is the alternative we don't really want to use
                                # DEMO_KEY has API rate limiting...
    return mykey.rstrip("\n")



def main():
    """run time code"""

    # grab our NASA key
    mykey = credget()
    print(mykey)

    # perform out API lookup
    apitolookup = f"{API}api_key={mykey}"
    
    resp = requests.get(apitolookup)
    if resp.status_code != 200:
        print(f"A non 200 code was returned: {resp.status_code}")
        sys.exit()

    print(resp.json())

    print(resp.json().get("hdurl"))
    print(resp.json().get("explanation"))

if __name__ == "__main__":
    main()
