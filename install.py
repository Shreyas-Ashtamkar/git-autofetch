import sys, os

if sys.version_info.major != 3:
    print("Python version 3 required to run this script")
    exit(1)

PYTHON_EXEC  = sys.executable
THIS_FOLDER  = os.path.dirname(__file__)

PROJECTS_LIST = './projectlist.py'

if not os.path.isfile(PROJECTS_LIST):
    xmlfile = open(PROJECTS_LIST, 'w') 
    xmlfile.write(\
        'from projects import _Project\n\n' \
        '# Create A Project Object for each and every project you want to auto fetch\n'\
        'PROJECT_LIST = [\n'\
        '    _Project(\n'\
        f'        path={THIS_FOLDER}\n'\
        '    )\n' \
        ']\n'
    )
    xmlfile.close()

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
