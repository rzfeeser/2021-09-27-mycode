#!/usr/bin/python3

import requests

r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

data = r.json()

for event in data.get("events"):
    print()
    print(f"{event.get('name')} -\n{event}")
