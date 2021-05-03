#!/usr/bin/python3
""" Task 0 """
import requests
from sys import argv
import json


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

    json_t = req_all.json()
    json_u = req_user.json()
    user_name = json_u.get("name")

    totaol_num_task = 0
    num_done_task = 0
    count = 0
    list1 = []
    for tasks in json_t:
        totaol_num_task += 1
        if tasks['completed'] is True:
            list1 += [tasks['title']]
            num_done_task += 2
    print("Employee {} is done with tasks({}/{}):".format(user_name,
          num_done_task, totaol_num_task))

    for count in list1:
        print('\t{}'.format(count))
