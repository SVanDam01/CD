![example workflow](https://github.com/SVanDam01/CD/actions/workflows/deploy.yml/badge.svg)

# CD Assignment

I have build a Continuous Deployment (CD) on a external server. Visit the server on http://167.172.98.135/.

## **What have I done?**

To accomplice the assignment I have build four components:

> - prepair the server
> - create a new repositorie on GitHub
> - create the content
> - create a GitHub Workflow (Actions)

### _prepair the server_

First I had to update the server via the CLI on the server. Affter that I had to pip install Python, Flask, NGINX and Gunicorn. To have the Flask server running (continouisly) I had to configurate de default .service file and the NGINX default file (located in the sites-available folder). I have created a SSH key and linked it to the server! Now I can log in without a password!

### _create a new repository on GitHub_

Yes, The server is running! now it is time to create a new repository on GitHub. It was late so I had no inspiration and call it 'CD'. After I had created this repository I logged in on the sever and execute a git clone command. BOOM! The depository is linked to the server!

### _create the content_

OK, lets create some content so I can show the world what I have learned! I am a big football fan so I create a small Flask app about dutch football fan chants.

### _create a GitHub Workflow (Actions)_

The assignment was to create a CD. So I have made a workflow bij GitHub Actions in a .yml file. The file is buildup in two parts. If annything is pushed to the main, a check is performed on a test_main.py. If the test is a succes, the changes are directly pulled bij de server via a .sh file on the server.

**_deploying.sh_**:

```sh
# Navigate to repository
echo "Navigating to repository"
cd /home/CD

# Pull github
echo "Pull from GitHub: https://github.com/SVanDam01/CD.git"
git pull

# Restart the application
echo "Restart application"
systemctl restart CD

# Check status
systemctl status CD

```

BAM! It's working! The site is running on the server and if a make a change in de repository, the server will be updated!

## **Which problems did I encountered along the way and how did I solved them**

OK, OK, I looks like it was easy peasy for me but no.... I had to face some issues in this process that I had to solve.

> - Why is the server not running my site?
> - How do I create a .sh file?
> - Why do I get an error when I pull the files from the repository?

### _Why is the server not running my site?_

In the course we had the create a Flask app 'farm'. The course explaned how to do so and it worked! I thought it was eassy to create a nother folder (home/CD), tweak some settings and run the new Flask app! But no... Only the farm app was running and I get errors when I was trying to run the CD app. But why?! It was super frustrating. I have ask questions in Slack, but I was not satisfied by given answers. After a two days I found teh solution online! With `systemctl stop farm`. Now the Flask server was avalible to run `systemctl enable --now CD`! And YES! The site was online!

### _How do I create a .sh file?_

I have search the web to find more about .sh. I found this video on YT (https://www.youtube.com/watch?v=czC8j9s-_wQ). So I have add all the lines that I had to type normally in de CLI and put it now in the .sh file!

### _Why do I get an error when I pull the files from the repository?_

I thought everything was working, but if I change something the files were not updated to the server! But why? GitHub was able to connect to the server by d private key and it was executing the .sh file! However, I got an error on the .sh file when uploading to the server. I had add the .sh file to the repository, but this generated a conflict on the server, because the same .sh was excuted! So I deleted the .sh file from the repository and tried it again.... Yes! Now it is working!
