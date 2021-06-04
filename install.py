import sys, os

if sys.version_info.major != 3:
    print("Python version 3 required to run this script")
    exit(1)

PYTHON_EXEC  = sys.executable
THIS_FOLDER  = os.path.dirname(__file__)

def create_file(file_name, text, replace=False):
    if not replace and os.path.isfile(f"{THIS_FOLDER}/{file_name}"):
        print(f"{file_name.replace('.',' ')} exists")
    else:
        print(f"creating {file_name.replace('.',' ')} file")
        with open(file_name, 'w') as file:
            file.write(text)

create_file(
file_name="autofetch.service", 
replace=True,
text=\
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
)

create_file(
file_name="projectlist.py", 
replace=False,
text= \
f'''
from projects import _Project

# Create A Project Object for each and every project you want to auto fetch
PROJECT_LIST = [
    _Project(
        path="{THIS_FOLDER}"
    ),
]
'''
)

create_file(
file_name="configs.py",
replace=False,
text='DELAY = 30'
)
