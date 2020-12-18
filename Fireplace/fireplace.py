'''
Created on June 1, 2017

@author: jeremyblythe
@author: bradsileo
'''
import pygame
import os
import pygameui as ui
import logging
import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

#client id and client secret
uri = 'https://graph.api.smartthings.com/api/smartapps/installations/e0a5f574-7335-46d4-9a78-b46e4410c82a'
access_token='ac626b44-b7b5-4108-9a8c-7718f568bbf4'

	
log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

MARGIN = 20

class PiTft(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)

        self.on17_button = ui.Button(ui.Rect(MARGIN, MARGIN, 130, 90), 'Next')
        self.on17_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.on17_button)

        self.on4_button = ui.Button(ui.Rect(170, MARGIN, 130, 90), 'red')
        self.on4_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.on4_button)

        self.off17_button = ui.Button(ui.Rect(MARGIN, 130, 130, 90), 'green')
        self.off17_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.off17_button)

        self.off4_button = ui.Button(ui.Rect(170, 130, 130, 90), 'off')
        self.off4_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.off4_button)
        logger.info("Finished Init")
		
		
    def gpi_button(self, btn, mbtn):
        logger.info("Button " + btn.text + " started")
        temp_url = uri + "/press/" + btn.text
        headers = { 'Authorization' : 'Bearer ' + access_token }
        r = requests.put(temp_url, headers=headers)
        logger.info("Button" + btn.text + " pressed - call:" + temp_url)        

ui.init('Raspberry Pi UI', (320,240))
pygame.mouse.set_visible(True)
ui.scene.push(PiTft())
ui.run()


