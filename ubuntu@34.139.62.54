#!/usr/bin/env bash
#Sets up your web servers for the deployment of web_static

apt -y update
apt -y install nginx

sudo ufw allow "Nginx HTTP"

sudo mkdir -p /data/web_static/shared /data/web_static/releases/test

echo "Holberton School" > /data/web_static/releases/test/index.html

ln -fns /data/web_static/releases/test /data/web_static/current

chown -hR ubuntu:ubuntu /data

sed -i '/^\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

sudo service nginx restart
