garageoPIner-server
===================

Server-side application for garageoPIner. Running this application on a raspberry pi allows you to control your garage doors(up to 2) with your smartphone. All you need is a relay and a few wires.


Things that need to be installed on your RPI
=============================================
###### For installing all the things you need on your raspberry pi, run the following commands:

sudo apt-get update

sudo apt-get install python-dev

sudo apt-get install python-pip

sudo pip install rpi.gpio Flask configparser

How to run the server side
=============================================
######Download this project.
wget https://github.com/wirthual/garageoPIner-server/archive/twoGarageDoors.zip

######Unzip downloaded folder:
unzip twoGarageDoors.zip

######Switch to the unziped folder where you find the file: garageoPIner.py
cd garageoPIner-server-master/

######Run the application
python garageoPIner.py

Thats it :)

Now you can see the web-interface on http://ipaddressofrpi:80

An android client you find here: https://github.com/wirthual/garageoPIner-androidApp
