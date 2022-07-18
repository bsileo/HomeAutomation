# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTime
from flask import Flask

import time
import requests
import logging

import smbus

# Maybe needed later to read GPIO status to update "current" mode display
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


uri ="http://192.168.2.106:39501"
access_token = ""

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)
fh = logging.FileHandler(r'fireplace_qt.log')
logger.addHandler(fh)

# This is our window from QtCreator
import mainwindow

touchTime = QTime(0,0,0)

# 52PI EP-0099 Relay
DEVICE_BUS = 1
DEVICE_ADDR = 0x10
		

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
	# access variables inside of the UI's file
	def __init__(self):
		super(self.__class__, self).__init__()
		self.sleeping = False
		self.setupUi(self) # gets defined in the UI file
		self.showFullScreen()
		self.setMouseTracking(True)
		global fireplace

		self.redButton.clicked.connect(fireplace.red)
		self.greenButton.clicked.connect(fireplace.green)
		self.blueButton.clicked.connect(fireplace.blue)
		self.purpleButton.clicked.connect(fireplace.purple)
		self.yellowButton.clicked.connect(fireplace.yellow)
		self.ltBlueButton.clicked.connect(fireplace.lightblue)
		self.whiteButton.clicked.connect(fireplace.white)
		self.offButton.clicked.connect(fireplace.off)

		self.startSleepTimer()

	def changedHeat(self):
		if (self.awake()):
			if (self.heatCheck.isChecked()):
				GPIO.output(23, 1)
				logger.info('Pressed Heat - ON')
			else:
				GPIO.output(23, 0)
				logger.info('Pressed Heat - OFF')

	def mouseMoveEvent(self, e):
		self.wakeup()
		# super(GraphicsView, self).mouseMoveEvent(e)

	def awake(self):
		return not self.sleeping

	def wakeup(self):
		global touchTime
		global fireplace

		touchTime.restart()
		logger.debug("Move event - reset touchTime and wake up")

		fireplace.wakeup()
		self.sleeping=False

	def startSleepTimer(self):
		global touchTime
		touchTime.start()
		self.sleepTimer()

	def sleepTimer(self):
		global touchTime
		global fireplace
		wait = 1*30*1000  # 1 minute

		logger.debug("Check sleep status--" + str(touchTime.elapsed()) + " >? " + str(wait))
		try:

			if (touchTime.elapsed() > wait):
				# go to sleep
				if (self.awake()):
					logger.info("Going to sleep")
					fireplace.sleep()
					self.sleeping=True
				else:
					logger.debug("still asleep")
		finally:
			# check every 30 seconds
			QTimer.singleShot(30*1000, self.sleepTimer)


class Fireplace:
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setup(17, GPIO.OUT, initial=1)
		GPIO.setup(27, GPIO.OUT, initial=1)
		GPIO.setup(22, GPIO.OUT, initial=1)
		GPIO.setup(23, GPIO.OUT, initial=1)
		GPIO.setup(18,GPIO.OUT)
		self.pi_pwm = GPIO.PWM(18,100)
		self.pi_pwm.start(100)
		self.bus = smbus.SMBus(DEVICE_BUS)

	def changedHeat(self):
		if (self.awake()):
			if (self.heatCheck.isChecked()):
				GPIO.output(23, 1)
				logger.info('Pressed Heat - ON')
			else:
				GPIO.output(23, 0)
				logger.info('Pressed Heat - OFF')

	def wakeup(self):
		self.pi_pwm.ChangeDutyCycle(100)

	def sleep(self):
		self.pi_pwm.ChangeDutyCycle(0)

	def off(self):
		self.setColorSwitches("lightoff",0,0,0)

	def red(self):
		self.setColorSwitches("red",0,0,1)

	def blue(self):
		self.setColorSwitches("blue",1,0,0)

	def lightblue(self):
		self.setColorSwitches("lightblue",1,1,0)

	def yellow(self):
		self.setColorSwitches("yellow",0,1,1)

	def purple(self):
		self.setColorSwitches("purple",1,0,1)


	def white(self):
		self.setColorSwitches("white",1,1,1)

	def green(self):
		self.setColorSwitches("green",0,1,0)

	def off(self):
		self.setColorSwitches("off",0,0,0)

	def setColorSwitches(self,color,sw1,sw2,sw3):
	   	#logger.debug("setSwitches " + color + " = " + sw1 + "," + sw2 +"," + sw3)
		GPIO.output(17, 0 if sw1 else 1)
		self.bus.write_byte_data(DEVICE_ADDR, 1, 0x00 if sw1 else 0xFF)
		GPIO.output(27, 0 if sw2 else 1)
		self.bus.write_byte_data(DEVICE_ADDR, 2, 0x00 if sw2 else 0xFF)
		GPIO.output(22, 0 if sw3 else 1)
		self.bus.write_byte_data(DEVICE_ADDR, 3, 0x00 if sw3 else 0xFF)
		url = uri + "/press/" + color
		data = {'color': color }
		headers = { 'Authorization' : 'Bearer ' + access_token }
		r = requests.put(url, headers=headers, json=data)
		logger.debug(r)


app = Flask(__name__)

@app.route('/red')
def red():
	global fireplace
	fireplace.red()
	return "{message:'Set to Red', status:1}"

@app.route('/blue')
def blue():
	global fireplace
	fireplace.blue()
	return "{message:'Set to Blue', status:1}"

@app.route('/lightblue')
def lightblue():
	global fireplace
	fireplace.lightblue()
	return "{message:'Set to Light Blue', status:1}"

@app.route('/yellow')
def yellow():
	global fireplace
	fireplace.yellow()
	return "{message:'Set to Yellow', status:1}"

@app.route('/purple')
def purple():
	global fireplace
	fireplace.purple()
	return "{message:'Set to Purple', status:1}"

@app.route('/white')
def white():
	global fireplace
	fireplace.white()
	return "{message:'Set to White', status:1}"

@app.route('/green')
def green():
	global fireplace
	fireplace.green()
	return "{message:'Set to Green', status:1}"

@app.route('/off')
def off():
	global fireplace
	fireplace.off()
	return "{message:'Set to Off', status:1}"

@app.route("/")
def main():
    app.logger.info("main route")
    return "Hello World!"

@app.before_first_request
def setup():
	global fireplace
	fireplace = Fireplace()


def main():
	global fireplace
	fireplace = Fireplace()
	qtapp = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	form.startSleepTimer()
	# without this, the script exits immediately.
	sys.exit(qtapp.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
	main()
