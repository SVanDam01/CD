# Navigate to repository on droplet
echo "Navigating to repository"
cd /home/farm

# Print current location
pwd

# Pull github code to here
echo "Git pull"
git pull

# Restart the application after we've pulled in new code
echo "restart application"
systemctl restart farm

# Check service status
systemctl status farm
