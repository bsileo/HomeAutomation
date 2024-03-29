# Pi Build
- Run Raspberry Pi Imager to setup SD Card
- See https://www.raspberrypi.org/documentation/configuration/wireless/headless.md
- Enable SSH - https://www.raspberrypi.org/documentation/remote-access/ssh/README.md $3
- sudo apt install samba samba-common-bin smbclient cifs-utils
  - Install SAMBA (optional) https://www.raspberrypi.org/documentation/remote-access/samba.md

- sudo apt-get install nodejs npm
  - Required to use PM2
  
  # Setup Info
  watch -n 1 cat /proc/net/wireless
  sudo apt-get install wavemon
  sudo wavemon
# HomeAutomation package install

git config --global  user.name "Brad Sileo"
git config --global  user.email "brad@sileo.name"
git config --global credential.helper 'cache --timeout=36000'
git clone https://github.com/bsileo/HomeAutomation.git

cd HomeAutomation

mkdir logs

## Python Devices 
- pip3 install influxdb
- pip3 install pigpio

// No longer need virtual environment

- // sudo apt install virtualenv python3-virtualenv -y

- // virtualenv -p /usr/bin/python3 pondflow

- // source pondflow/bin/activatesudo apt-get install wavemon


### Testing
- python pondflow-hubitat_influx.py


# Auto Startup of Apps on Device
sudo npm install pm2@latest -g

pm2 install pm2-logrotate

### Python 
sudo systemctl enable pigpiod

sudo systemctl start pigpiod 

pm2 start pondflow-hubitat_influx.py --name pondflow --interpreter python3
pm2 start pondtemp-hubitat_influx.py --name pondtemp --interpreter python3
pm2 start PondTemperatureMultiHubitat.py --name pondtemp --interpreter python3

pm2 save 

pm2 startup
- follow resulting prompt to cut and paste command
  
# Temp Probe Wiring
[Connected via resistor board](https://smile.amazon.com/dp/B087JQ6MCP?psc=1&ref=ppx_pop_dt_b_product_details)

Red ------------- 3.3V (pin 1)

Black ----------- Ground (pin 20 )

Yellow ------------- GPIO 4 (pin 7)
