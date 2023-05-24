# Navigate to repository
echo "Navigating to repository"
cd /home/CD

# Pull github
echo "Pull github: https://github.com/SVanDam01/CD.git"
git pull

# Restart the application
echo "Restart application"
systemctl restart CD

# Check status
systemctl status CD
