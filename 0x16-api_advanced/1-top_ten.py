#!/usr/bin/python3
import requests


def top_ten(subreddit):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)\
                  AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                     .format(subreddit), headers=headers)
    if r.status_code == 200:
        r = r.json()
        childrens = r.get('data').get('children')
        for x in childrens:
            print(x.get('data').get('title'))
    else:
        print('None')
