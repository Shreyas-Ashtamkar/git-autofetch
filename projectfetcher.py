#!/usr/bin/python3
from os import system as run
from multiprocessing import Process
from projectlist import PROJECT_LIST


PROJECT_COUNT = len(PROJECT_LIST)
if PROJECT_COUNT == 1:
    print(f"There is 1 project registered.")
else:
    print(f"There are {PROJECT_COUNT} projects registered.")

def fetch():
    for project in PROJECT_LIST:
        print("updating :", project)
        if project.creds:
            project.url.replace('github.com', f'{project.creds["username"]}:{project.creds["password"].replace("@","%40")}@github.com')
        Process(
            target=run, 
            args=(f"cd {project.path} && git pull {project.url}",)
        ).start()

if __name__ == '__main__':
    fetch()
