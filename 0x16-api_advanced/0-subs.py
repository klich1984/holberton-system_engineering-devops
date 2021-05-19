#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
from requests import get


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of"""

    res = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
              headers={"User-Agent": "Klich from Holberton"},
              allow_redirects=False)
    # print(res)
    if res.status_code == 200:
        number_of_subscribers = res.get('data').get('subscribers')
        print(number_of_subscribers, type(number_of_subscribers))
        return number_of_subscribers
    else:
        return 0
