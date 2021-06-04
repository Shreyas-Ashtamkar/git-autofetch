# git-autofetch
A simple script to automatically update the selected github repositories on a set time interval, very usefull for sending code to Raspberry-Pi

## USAGE
1. Clone this repo.
    ![cloning the repo](./project-screenshots/git-clone.png)

2. cd into the repo
    ![cloning the repo](./project-screenshots/cd-git-autofetch.png)

3. Run the install.py.
    ![cloning the repo](./project-screenshots/install.png)

4. Register Projects in the newly created projectlist.py
    
    ![cloning the repo](./project-screenshots/edit-projectlist.png)

5. Move the newly created autofetcher.service to systemd's folders.
    
    run `sudo mv autofetch.service /lib/systemd/system/`
    ![cloning the repo](./project-screenshots/register-service.png)

6. Reload the systemd daemon.
    
    run `sudo systemctl daemon-reload`
    ![cloning the repo](./project-screenshots/daemon-reload.png)

7. Start the service autofetcher.service

    run `sudo systemctl start autofetcher`
    ![cloning the repo](./project-screenshots/start-service.png)

8. Check the status of autofetcher service

    run `sudo systemctl status autofetcher`
    ![cloning the repo](./project-screenshots/status-service.png)

8. (optional) Enable the service autofetcher

    run `sudo systemctl enable autofetcher`
