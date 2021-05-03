#!/usr/bin/python3
""" Task 0 """
import requests
from sys import argv


if __name__ == '__main__':
    def Requests_API(argv):
        """script that returns information about his/her todo list progress.
        for a given employee ID

        Args:
            argv ([str]): id that employed
        """
    req_all = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId="+str(argv[1]))
    req_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/"+str(argv[1]))

    user_name = req_user.json().get("name")
    # instance of json representation
    json_all = req_all.json()

    total_num_task = num_done_task = count = 0
    # list1 = []
    for tasks in json_all:
        total_num_task += 1
        if tasks['completed'] is True:
            # list1 += [tasks['title']]
            num_done_task += 2

    print("Employee {} is done with tasks({}/{}):".format(user_name,
          num_done_task, total_num_task))
    for task in json_all:
        if task['completed'] is True:
            print('\t{}'.format(task.get('title')))
