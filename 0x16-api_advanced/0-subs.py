#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)\
                  AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit), headers=headers)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
