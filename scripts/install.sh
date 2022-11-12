# ----------------------------------------------------------------

echo "Welcome to StarLand Install script"
echo "================================================"
echo "Version : 1.0.0"
echo "Author : Max Qian"
echo "License : MIT License"

system = uname -a
echo "System : $system"

# ----------------------------------------------------------------

# Update All Software , make sure all newest

echo "================================================"
echo "Start update all software"
sudo apt-get update && sudo apt-get upgrade -y
echo "Finish update"
echo "================================================"

# ----------------------------------------------------------------

# Install INDI & Handware Driver
echo "================================================"
echo "Install INDI & Handware Driver & All dependencies"
sudo apt-add-repository ppa:mutlaqja/ppa
sudo apt-get update
sudo apt-get install -y indi-full gsc
echo "Finish install INDI & Handware Driver"
echo "================================================"

# ----------------------------------------------------------------

# Install Kstars

echo "================================================"
echo "Start Install Kstars"
sudo apt-get install -y kstars-bleeding
echo "Finish Install Kstars"
echo "================================================"

# ----------------------------------------------------------------

# Install PHD2 Guider Software

echo "================================================"
echo "Start Install PHD2"

# If phd2 is not found, try phd2-bin
sudo add-apt-repository ppa:pch/phd2
sudo apt update
sudo apt-get install -y phd2

echo "Finish Install PHD2"
echo "================================================"

# ----------------------------------------------------------------

# Install Nginx for Web Application

echo "================================================"
echo "Start Install Nginx"
sudo apt-get install -y nginx
echo "Finish Install Nginx"
echo "================================================"

# ----------------------------------------------------------------

# Install Python3
echo "================================================"
echo "Start Install Python3"
sudo apt-get install -y python3
echo "Finish Install Python3"
echo "================================================"

# ----------------------------------------------------------------

