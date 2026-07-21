#!/usr/bin/env python3
"""function create a method that returns the list of ships"""

import requests


def availableShips(passengerCount):
    """If no ship available, return an empty list."""
    url = "https://swapi-api.hbtn.io/api/starships/"
    result = []
    while url:
        response = requests.get(url)
        dict1 = response.json()

        for ship in dict1["results"]:
            passengers = ship["passengers"].replace(",", "")
            if passengers.isdigit():
                if int(passengers) >= passengerCount:
                    result.append(ship["name"])
        url = dict1["next"]
    return result
