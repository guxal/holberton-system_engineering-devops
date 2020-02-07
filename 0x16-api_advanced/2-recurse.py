#!/usr/bin/python3
'''
Recurse function find the title in the many pages
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)\
                  AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}

    if after is None:
        request = requests.get('https://www.reddit.com/r/{}/hot.json?limit=100'
                               .format(subreddit), headers=headers)
        if request.status_code != 200:
            return None
        data = request.json().get('data')
        childrens = data.get('children')
        if not childrens:
            return None
        hot_list += [c.get('data').get('title') for c in childrens]
        recurse(subreddit, hot_list, data.get('after'))
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
        request = requests.get(url.format(subreddit, after), headers=headers)
        data = request.json().get('data')
        childrens = data.get('children')
        hot_list += [children.get('data').get('title')
                     for children in childrens]
        if data.get('after') is None:
            return hot_list
        else:
            recurse(subreddit, hot_list, data.get('after'))
    return hot_list
