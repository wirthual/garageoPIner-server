garageoPIner-server
===================

Server-side application for garageoPIner. Running this application on a raspberry pi allows you to control your garage doors(up to 2) with your smartphone. All you need is a relay and a few wires.


Things that need to be installed on your RPI
---------------------------------------------
###### For installing all the things you need on your raspberry pi, run the following commands:

```bash
sudo apt-get update

sudo apt-get install python-dev

sudo apt-get install python-pip

sudo pip install rpi.gpio Flask configparser
```

How to run the server side
----------------------------------------
######Download this project.
```bash
wget https://github.com/wirthual/garageoPIner-server/archive/twoGarageDoors.zip
```
######Unzip downloaded folder:
```bash
unzip twoGarageDoors.zip
```

######Switch to the unziped folder where you find the file: garageoPIner.py
```bash
cd garageoPIner-server-twoGarageDoors/
```

######Change the config
Edit garageoPIner.config for your needs:
```bash
[Settings]
port = 80 # port garageoPIner is running on
pin1 = 4  # pin for toggle door1
pin2 = 17 # pin for toggle door2

[Credentials]
username = admin # username for authentication on webpage and app
password = garageopiner # password for authentication on webpage and app
```

######Run the application
```bash
python garageoPIner.py &
```

Thats it :)

Now you can see the web-interface on http://ipaddressofrpi:80

An android client you find here: https://github.com/wirthual/garageoPIner-androidApp
