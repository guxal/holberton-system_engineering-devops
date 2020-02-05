#!/usr/bin/python3
'''This script take data of the employee test'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    routes = ['users/{}', 'todos?userId={}', 'todos?userId={}&completed=true']

    argv = sys.argv

if len(argv) > 1:
    user = requests.get(url + routes[0].format(argv[1]))
    allTask = requests.get(url + routes[1].format(argv[1]))
    doneTask = requests.get(url + routes[2].format(argv[1]))

    name = user.json().get('name')
    numberDoneTask = len(doneTask.json())
    numberAllTask = len(allTask.json())

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(name, numberDoneTask, numberAllTask))

    for done in doneTask.json():
        print('\t' + done.get('title'))
