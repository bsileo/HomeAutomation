#!/bin/bash

export FLASK_APP=~/HomeAutomation/Fireplace/fireplace_qt.py
cd /home/pi/HomeAutomation/Fireplace
/usr/bin/flask run --host=0.0.0.0 >> ~/flask_api.log


