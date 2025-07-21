#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit.
If subreddit is invalid, returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a subreddit, or 0 if invalid."""
    if not isinstance(subreddit, str) or subreddit == "":
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alx-api-advanced:v1.0 (by /u/your_username)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
