#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit"""
    res = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
              headers={"User-Agent": "Klich from Holberton"},
              allow_redirects=False, params={"limit": 10})
    # print(res)
    if res.status_code == 200:
        for children in res.json().get('data').get('children'):
            # print(children)
            print(children.get('data').get('title'))
    else:
        print(None)
