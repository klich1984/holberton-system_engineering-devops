#!/usr/bin/python3
""" Task 1 """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    def Requests_API(argv):
        """script that export data in the CSV format.

        Args:
            argv ([str]): id that employed
        """
    req_all = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId="+str(argv[1]))
    req_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/"+str(argv[1]))

    user_name = req_user.json().get("username")
    # instance of json representation
    json_all = req_all.json()

    with open('{}.csv'.format(argv[1]), 'w') as f:
        f_write = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in json_all:
            f_write.writerow([argv[1], user_name, task.get(
                'completed'), task.get('title')])
