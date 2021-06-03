#!/usr/bin/python3
from os import system as run
from projects import PROJECT_LIST
from multiprocessing import Process

def fetch():
    for project in PROJECT_LIST:
        print("updating :", project)
        Process(target=run,args=(f"cd {project.path} && git pull --recurse-submodules",)).start()

if __name__ == '__main__':
    fetch()
