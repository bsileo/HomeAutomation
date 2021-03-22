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

app = Flask(__name__)


# This is our window from QtCreator
import mainwindow

touchTime = QTime(0,0,0)
pi_pwm = 0
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
	# access variables inside of the UI's file
	def __init__(self):
		super(self.__class__, self).__init__()
		self.sleeping = False
		self.setupUi(self) # gets defined in the UI file
		self.showFullScreen()
		self.setMouseTracking(True)

		self.redButton.clicked.connect(self.pressedredButton)
		self.greenButton.clicked.connect(self.pressedgreenButton)
		self.blueButton.clicked.connect(self.pressedblueButton)
		self.purpleButton.clicked.connect(self.pressedpurpleButton)
		self.yellowButton.clicked.connect(self.pressedyellowButton)
		self.ltBlueButton.clicked.connect(self.pressedltBlueButton)
		self.whiteButton.clicked.connect(self.pressedwhiteButton)
		self.offButton.clicked.connect(self.pressedoffButton)


	def pressedredButton(self):
		self.gpi_button(self,'red')

	def pressedgreenButton(self):
		self.gpi_button(self,'green')

	def pressedblueButton(self):
		self.gpi_button(self,'blue')

	def pressedpurpleButton(self):
		self.gpi_button(self,'purple')

	def pressedwhiteButton(self):
		self.gpi_button(self,'white')

	def pressedltBlueButton(self):
		self.gpi_button(self,'lightblue')

	def pressedyellowButton(self):
		self.gpi_button(self,'yellow')

	def pressedoffButton(self):
		self.gpi_button(self,'off')

	def changedHeat(self):
		if (self.awake()):
			if (self.heatCheck.isChecked()):
				GPIO.output(23, 1)
				logger.info('Pressed Heat - ON')
			else:
				GPIO.output(23, 0)
				logger.info('Pressed Heat - OFF')

	def awake(self):
		return not self.sleeping

	def gpi_button(self, this, btn):
		if (self.awake()):
			logger.info("Button " + btn + " pressed")
			QApplication.setOverrideCursor(Qt.WaitCursor);
			temp_url = uri + "/press/" + btn
			headers = { 'Authorization' : 'Bearer ' + access_token }
			#r = requests.put(temp_url, headers=headers)
			logger.debug("Button" + btn + " pressed - call:" + temp_url)
			eval("self." + btn + "()")
			QApplication.restoreOverrideCursor()
		else:
			self.wakeup()
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

	def setColorSwitches(self,color,sw1,sw2,sw3):
	   #logger.debug("setSwitches " + color + " = " + sw1 + "," + sw2 +"," + sw3)
	   GPIO.output(17, 0 if sw1 else 1)
	   GPIO.output(27, 0 if sw2 else 1)
	   GPIO.output(22, 0 if sw3 else 1)

	def mouseMoveEvent(self, e):
		self.wakeup()
		# super(GraphicsView, self).mouseMoveEvent(e)

	def wakeup(self):
		global touchTime
		global pi_pwm

		touchTime.restart()
		logger.debug("Move event - reset touchTime and wake up")

		# and wake up
		pi_pwm.ChangeDutyCycle(100)
		self.sleeping=False

	def startSleepTimer(self):
		global touchTime
		touchTime.start()
		self.sleepTimer()

	def sleepTimer(self):
		global touchTime
		global pi_pwm
		wait = 1*60*1000  # 1 minute

		logger.debug("Check sleep status--" + str(touchTime.elapsed()) + " >? " + str(wait))
		try:

			if (touchTime.elapsed() > wait):
				# go to sleep
				if (self.awake()):
					logger.info("Going to sleep")
					pi_pwm.ChangeDutyCycle(0)
					self.sleeping=True
		finally:
			# check every 5 seconds
			QTimer.singleShot(5*1000, self.sleepTimer)


# I feel better having one of these


def main():
	global pi_pwm
	global form
	GPIO.setup(17, GPIO.OUT, initial=1)
	GPIO.setup(27, GPIO.OUT, initial=1)
	GPIO.setup(22, GPIO.OUT, initial=1)
	GPIO.setup(23, GPIO.OUT, initial=1)
	GPIO.setup(18,GPIO.OUT)
	pi_pwm = GPIO.PWM(18,100)
	pi_pwm.start(100)
	# a new app instance
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	form.startSleepTimer()

	# without this, the script exits immediately.
	sys.exit(app.exec_())

@app.route('/red')
def red()
	form.red(form)


# python bit to figure how who started This
if __name__ == "__main__":
	main()