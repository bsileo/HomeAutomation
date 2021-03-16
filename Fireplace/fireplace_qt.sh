# export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb1
# export QT_QPA_EVDEV_TOUCHSCREEN_PARAMETERS=/dev/input/touchscreen:rotate=90
export DISPLAY=:0
#export QT_QPA_FB_TSLIB=1
#export TSLIB_FBDEVICE=/dev/fb1
#export TSLIB_TSDEVICE=/dev/input/touchscreen

#python3 fireplace_qt.py -platform linuxfb:fb=/dev/fb1
python3 ~/HomeAutomation/Fireplace/fireplace_qt.py >> ~/fireplace_qt.log


