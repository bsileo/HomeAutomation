#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home


/usr/bin/gpio export 17 out
/usr/bin/gpio export 27 out
/usr/bin/gpio export 22 out
/usr/bin/gpio export 23 out

/usr/bin/gpio -g write 17 1
/usr/bin/gpio -g write 27 1
/usr/bin/gpio -g write 22 1
/usr/bin/gpio -g write 23 1


cd /
cd home/pi
sudo python firebuttons.py
cd /
