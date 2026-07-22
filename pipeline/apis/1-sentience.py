#!/usr/bin/env python3
"""method that returns list of names home planets for all sentient species"""

import requests


def sentientPlanets():
    """sentient type is in the classification or designation attributes"""
    url = "https://swapi-api.hbtn.io/api/species/"
    result = []
    while url:
        response = requests.get(url)
        dict1 = response.json()

        for i in dict1["results"]:
            designation = i.get("designation", "").lower()
            classification = i.get("classification", "").lower()
            if designation == "sentient" or classification == "sentient":
                homeworld_url = i["homeworld"]
                if homeworld_url:
                    planet_response = requests.get(homeworld_url)
                    planet_data = planet_response.json()
                    planet_name = planet_data["name"]
                    if planet_name not in result:
                        result.append(planet_name)
        url = dict1["next"]
    return result
