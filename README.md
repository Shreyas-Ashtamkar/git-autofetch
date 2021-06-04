# git-autofetch
A simple script to automatically update the selected github repositories on a set time interval, very usefull for sending code to Raspberry-Pi

## USAGE
1. Clone this repo wherever you want, edit the projects.py file, add desired projects and start the service.
2. Run the install.py.
3. Register Projects in the newly created projectlist.py
4. Move the newly created projectfetcher.service to systemd.
5. Reload the systemd daemon.
6. Enable the service projectfetcher.service
7. Start the service projectfetcher
