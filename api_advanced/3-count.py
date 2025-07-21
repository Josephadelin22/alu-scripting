#!/usr/bin/python3
"""
Recursively count occurrences of given keywords in all hot post titles of a subreddit.
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries Reddit API recursively, parses all hot article titles,
    and prints sorted count of keywords (case-insensitive, space delimited).
    """
    if counts is None:
        # Make lowercase and merge duplicates in word_list
        base_list = [w.lower() for w in word_list]
        counts = {w: 0 for w in base_list}
    if subreddit is None or subreddit == "" or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alx-api-advanced:v1.0 (by /u/your_username)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "")
            # Split the title into words, ignoring punctuation at end or start
            words = title.lower().split()
            for word in words:
                # Only count if it's exactly in counts (no punctuation attached)
               
                if word in counts:
                    counts[word] += 1

        next_after = data.get("data", {}).get("after")
        if next_after:
            return count_words(subreddit, word_list, after=next_after, counts=counts)
        else:
            # Print sorted results (descending by count, then alpha)
            filtered = [(w, c) for w, c in counts.items() if c > 0]
            # First sort by word alpha, then by count descending
            filtered.sort(key=lambda x: (-x[1], x[0]))
            for word, count in filtered:
                print("{}: {}".format(word, count))
            return

    except Exception:
        return
