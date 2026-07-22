#!/usr/bin/env python3
"""
Script that prints the location of a specific GitHub user/URL.
"""
import sys
import requests
import time


def fetch_location():
    """ Script that prints the location of a specific GitHub user/URL. """
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]
    try:
        r = requests.get(url)
    except Exception:
        return

    status = r.status_code

    if status == 200:
        # Fetch location key from JSON response
        data = r.json()
        location = data.get('location')
        if location:
            print(location)
    elif status == 404:
        print("Not found")
    elif status == 403:
        # Calculate reset time in minutes
        reset_time = int(r.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        minutes = (reset_time - current_time) // 60
        print(f"Reset in {minutes} min")


if __name__ == '__main__':
    fetch_location()
