#!/usr/bin/env python3
""" write a script that prints the location of a specific user """
import sys
import requests
import time


def get_user_location():
    """ user is passed as first argument of the script with the full API URL"""
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        location = json_data.get("location")
        if location:
            print(location)
        else:
            print("No location")
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_timestamp = int(response.headers.get("X-Ratelimit-Reset", 0))
        current_timestamp = int(time.time())

        reset_seconds = reset_timestamp - current_timestamp
        reset_minutes = int(reset_seconds / 60)
        print(f"Reset in {reset_minutes} min")
    if __name__ == "__main__":
        get_user_location()
