#!/usr/bin/env python3

astro = {"message": "success", "number": 5, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}, {"craft": "ISS", "name": "Doug Hurley"}, {"craft": "ISS", "name": "Bob Behnken"}]}

x = "People in Space:" (astro["number"])


for x in astro["people"]:
    print(f"{x['name']} is on the {x['craft']}")





