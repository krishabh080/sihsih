#!/bin/bash

# Install Git
yum install git -y

# Clone the repository
git clone https://github.com/krishabh080/sihsih.git

# Install Apache HTTP Server
yum install httpd -y

# Start Apache HTTP Server
systemctl start httpd

# Check Python version
python3 --version

# Install firewalld
yum install firewalld -y

# Stop firewalld
systemctl stop firewalld

# Check status of firewalld
systemctl status firewalld

# Start Apache HTTP Server
systemctl start httpd

# Install Python3 pip
yum install python3-pip -y

# Install Python packages
pip3 install joblib pickle-mixin regex nltk

# Download NLTK data
python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"

# Install TensorFlow version 2.11
pip install tensorflow==2.12

# Move necessary files to Apache CGI directory
cd sihsih/
mv final_json.py /var/www/cgi-bin/
mv stemm.py /var/www/cgi-bin/
mv stopwords.txt /var/www/cgi-bin/

# Set permissions for stopwords.txt
chown apache:apache /var/www/cgi-bin/stopwords.txt

#transfer the model from local system through scp and then run the chown commands for that also.
