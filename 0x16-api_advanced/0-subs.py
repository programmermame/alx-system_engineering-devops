#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "ALX"},
                            allow_redirects=False)
    if sub_info.status_code != 200:
        return 0

    try:
        data = sub_info.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except KeyError:
        # If the expected data structure is not found, return 0
        return 0

