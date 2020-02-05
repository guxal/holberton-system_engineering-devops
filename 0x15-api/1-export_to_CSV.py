#!/usr/bin/python3
'''This script take data of the employee test and
   create format csv with info all task '''
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    routes = ['users/{}', 'todos?userId={}', 'todos?userId={}&completed=true']

    argv = sys.argv

    if len(argv) > 1:
        id = argv[1]
        user = requests.get(url + routes[0].format(id))
        allTask = requests.get(url + routes[1].format(id))
        doneTask = requests.get(url + routes[2].format(id))

        name = user.json().get('name')
        numberDoneTask = len(doneTask.json())
        numberAllTask = len(allTask.json())

        print("Employee {} is done with tasks({:d}/{:d}):"
              .format(name, numberDoneTask, numberAllTask))

        for done in doneTask.json():
            print('\t ' + done.get('title'))

        with open(argv[1] + '.csv', 'w', newline='')as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for task in allTask.json():
                datasave = [id, name, task.get('completed'), task.get('title')]
                csvwriter.writerow(datasave)
