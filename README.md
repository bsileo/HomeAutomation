# Pi Install
- See https://www.raspberrypi.org/documentation/configuration/wireless/headless.md
- Enable SSH - https://www.raspberrypi.org/documentation/remote-access/ssh/README.md $3
- Install SAMBA (optional) https://www.raspberrypi.org/documentation/remote-access/samba.md
  

# HomeAutomation package install

git config --global  user.name "Brad Sileo"
git config --global  user.email "brad@sileo.name"
git clone https://github.com/bsileo/HomeAutomation.git
   Username: bsileo
   Password: 64eb61c8427e926670248aafa81c04f19ba93623  (Access Token from https://github.com/settings/tokens)

cd HomeAutoMation
mkdir logs

sudo apt-get install pm2

## Python Devices 
- sudo apt install virtualenv python3-virtualenv -y
- virtualenv -p /usr/bin/python3 pondflow
- source pondflow/bin/activate
- pip3 install influxdb
- pip3 install pigpio
  

sudo pigpiod
python pondflow-hubitat_influx.py

