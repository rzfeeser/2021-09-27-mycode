#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Send HTTP GET to API http://api.open-notify.org/astros.json"""

## standard library imports
import sys

## 3rd party imports
# python3 -m pip install requests
import requests

# python3 -m pip install pandas
import pandas

# vars defined within hte GLOBAL space
# are const
API = 'http://api.open-notify.org/astros.json'


def main():

    # Send HTTP GET to our API
    r = requests.get(API)

    # Get back 200 + JSON
    if r.status_code != 200:
        sys.exit("API response was a non-200.")

    # Strip out the JSON / grab json off the response
    astroData = r.json()

    # test our responses / test our code upto here...
    #print(type(astroData))
    #print(astroData)

    # Transform JSON into pythonic data
    # pull data into Pandas dataframe
    df = pandas.DataFrame.from_dict(astroData)

    # test our code up to here...
    #print(type(df))
    #print(df.head())

    # create a CSV file with our dataframe
    df.to_csv("/home/student/static/astroData.csv")

    # create a XLSX file with our dataframe
    df.to_excel("/home/student/static/astroData.xlsx")

    # create a markdown file with our dataframe
    # requires: python3 -m pip install tabulate
    # df.to_markdown("/home/student/static/astroData.md")

    # create a ... (find the link to all the types pandas works with) dataframe
    # see: https://pandas.pydata.org/docs/reference/api/ for all details on how

if __name__ == "__main__":
    main()
