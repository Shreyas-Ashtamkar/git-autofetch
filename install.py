import sys, os

if sys.version_info.major != 3:
    print("Python version 3 required to run this script")
    exit(1)

PYTHON_EXEC  = sys.executable
THIS_FOLDER  = os.path.dirname(__file__)

PROJECTS_LIST = './project_list.py'

if not os.path.isfile(PROJECTS_LIST):
    xmlfile = open(PROJECTS_LIST, 'w') 
    xmlfile.write('PROJECT_LIST = []')

service_script = \
f'''[Unit]
Description=Github Projects Auto Fetcher
After=multi-user.target
# Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart={PYTHON_EXEC} {THIS_FOLDER if THIS_FOLDER else '.' }/autofetch.py
# StandardInput=tty-force

[Install]
WantedBy=multi-user.target
'''

with open("autofetch.service",'w') as SERVICE_FILE:
    SERVICE_FILE. write(service_script)
