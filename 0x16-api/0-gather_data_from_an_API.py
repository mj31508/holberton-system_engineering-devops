#!/usr/bin/python3
"""Python script for a restful api"""
import requests
import sys

if __name__ == "__main__":

    """tasks"""

    # name = ""
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(url)
    user_dict = req.json()
    for user in user_dict:
        if int(user.get("id")) == int(user_id):
            name = user.get("name")
            break
    url1 = "https://jsonplaceholder.typicode.com/todos"
    req1 = requests.get(url1)
    task_dict = req1.json()
    d_tasks = 0
    t_tasks = 0
    task_titles = []
    for tasks in task_dict:
        if int(tasks.get("userId")) == int(user_id):
            t_tasks += 1
            if tasks.get("completed") is True:
                d_tasks += 1
                task_titles.append(tasks.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        name, d_tasks, t_tasks))

    for task in task_titles:
        print("\t {}".format(task))
