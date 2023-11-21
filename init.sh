#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install fail2ban -y
sudo apt-get install curl -y

sudo curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -

sudo apt-get install -y nodejs

npm i cypress cypress-localstorage-commands cypress-multi-reporters mocha mochawesome mochawesome-merge mochawesome-report-generator --save-dev
#pour le backup distant avec restic

mkdir ../container-backup/

sudo cp /etc/fail2ban/jail.{conf,local}

sudo apt install iptables -y

#Allow connections en route
#iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
#iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

#sudo iptables -A OUTPUT -p tcp --sport 22 --ctstate ESTABLISHED -j ACCEPT

echo "DROPPING CONNEXTIONS"

#Drop all conections
#sudo iptables -t filter -P INPUT DROP
#sudo iptables -t filter -P FORWARD DROP
#sudo iptables -t filter -P OUTPUT DROP

#Allow loopbacks
#sudo iptables -t filter -A INPUT -i lo -j ACCEPT
#sudo iptables -t filter -A OUTPUT -o lo -j ACCEPT

#CADDY
#sudo iptables -t filter -A OUTPUT -p tcp --dport 80 -j ACCEPT
#sudo iptables -t filter -A INPUT -p tcp --dport 80 -j ACCEPT

#sudo iptables -t filter -A OUTPUT -p tcp --dport 443 -j ACCEPT
#sudo iptables -t filter -A INPUT -p tcp --dport 443 -j ACCEPT

#DJANGO
#sudo iptables -t filter -A OUTPUT -p tcp --dport 8888 -j ACCEPT
#sudo iptables -t filter -A INPUT -p tcp --dport 8888 -j ACCEPT

#DJANGO
#sudo iptables -t filter -A OUTPUT -p tcp --dport 5173 -j ACCEPT
#sudo iptables -t filter -A INPUT -p tcp --dport 5173 -j ACCEPT

#DB
#sudo iptables -t filter -A OUTPUT -p tcp --dport 5432 -j ACCEPT
#sudo iptables -t filter -A INPUT -p tcp --dport 5432 -j ACCEPT

#SSH
#sudo iptables -t filter -A INPUT -p tcp --dport 2211 -j ACCEPT
#sudo iptables -t filter -A OUTPUT -p tcp --dport 2211 -j ACCEPT

echo "SAVING CONFIG"

#sudo iptables-save >/etc/sysconfig/iptables

#sudo service iptables restart

echo "CHANGING SSH PORT"

#sed -i 's/Port\ 22/Port\ 2211/g' /etc/ssh/sshd_config
#sed -i 's/PermitRootLogin\ yes/PermitRootLogin\ no/g' /etc/ssh/sshd_config
#service ssh restart

sudo apt install rclone
rclone config

sudo apt-get install restic

restic -r rclone:remote:backup-web init

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt install docker.io
systemctl start docker
systemctl enable docker

sudo docker-compose -f docker-compose.prod.yml up --build -d

sudo docker exec django python manage.py migrate
sudo docker exec django python populate.py

chmod 700 backup.sh
