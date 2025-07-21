#!/usr/bin/python3
"""
Recursive function to get all hot article titles of a subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list of titles
    of all hot articles for a given subreddit. Returns None if not valid.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alx-api-advanced:v1.0 (by /u/your_username)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        # Check if there's another page
        next_after = data.get("data", {}).get("after")
        if next_after is not None:
            return recurse(subreddit, hot_list, next_after)
        return hot_list
    except Exception:
        return
