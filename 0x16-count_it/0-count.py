#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
"""
from collections import Counter, defaultdict
import re
import requests

def count_words(subreddit, word_list, res=defaultdict(int), after=None):
    """count_words function"""
    headers = {"User-Agent": "api"}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    try:
        req = requests.get(url, headers=headers, allow_redirects=False).json()
        titles = req.get('data').get('children')
        for title in titles:
            count = Counter(title.get('data').get('title').lower().split(' '))
            for x in word_list:
                if x.lower() in count:
                    res[x.lower()] += count.get(x.lower())
        after = req.get('data').get('after')
        if after:
            return count_words(subreddit, word_list, res, after)
        sort_first = sorted(res.items(), key=lambda x: x[0])
        for k, v in sorted(sort_first, key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(k, v))
    except:
        return
