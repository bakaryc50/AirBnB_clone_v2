#!/usr/bin/env bash
#Sets up your web servers for the deployment of web_static

apt update
apt -y install nginx

ufw allow "Nginx HTTP"

mkdir -p /data/web_static/shared /data/web_static/releases/test

cat > /data/web_static/releases/test/index.html << 'EOF'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

ln -fns /data/web_static/releases/test /data/web_static/current

chown -hR ubuntu:ubuntu /data

sed -i '/^\tlisten 80 default_server;$/i location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

service nginx restart
