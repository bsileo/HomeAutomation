import glob
import hashlib
import sched
import time
import datetime
import threading
import requests
import logging
from logging.handlers import RotatingFileHandler
import json
from influxdb import InfluxDBClient
import pigpio

# Set this variables, influxDB should be localhost on Pi
host = "server1"
port = 8086
user = "admin"
password = "root"
# The database we created
dbname = "pondtemp"
session = "pond"
now = datetime.datetime.now()
runNo = now.strftime("%Y%m%d%H%M")
# Create the InfluxDB object
#client = InfluxDBClient(host, port, user, password, dbname,False,False,3)
corlysisClient = InfluxDBClient(host='corlysis.com', port=port, username='token',password='48abd1cc8081ae4bdd109e170c047040',
    database='pond',ssl=True,verify_ssl=False,timeout=15,retries=3)
print ("Session: ", session)
print ("runNo: ", runNo)

logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,
                    format='{%(asctime)s}[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
logger = logging.getLogger('my_logger')
logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,
                    format='{%(asctime)s}[%(levelname)s] %(message)s',
                    )
handler = RotatingFileHandler('./logs/PondFlow.log', maxBytes=10000, backupCount=10)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# logger.addHandler(handler)

class FlowSensor(object):
    WATERFLOW = 0
    old_count   = 0
    flowCallback = 0
    def __init__(self):
        flowGpio = 17
        pi = pigpio.pi()
        pi.set_mode(flowGpio, pigpio.INPUT)
        pi.set_pull_up_down(flowGpio, pigpio.PUD_DOWN)
        self.flowCallback = pi.callback(flowGpio, pigpio.FALLING_EDGE)

    def get_flow(self):
        count = self.flowCallback.tally()
        self.flowCallback.reset_tally()
        logger.debug("counted {} pulses".format(count))
        return count


class SampleHandler():
    INTERVAL_SECONDS = 60
    FLOW = 0
    def __init__(self):
        self.FLOW = FlowSensor()

    def _timer_loop(self):
        hURL ='http://192.168.2.106/apps/api/417/devices/'
        while True:
            logger.info('Start logging run')
            f = self.FLOW.get_flow()
            liters = f * 0.10
            hIdxURL = hURL + '611' + '/setFlowPulses/' + str(f) + '?access_token=c82410cc-4e3b-4eb2-8055-bf3ff4e55678'
            try:
                logger.debug('Send FLOW to Hubitat - ' + hIdxURL)
                resp = requests.get(hIdxURL, timeout=3)
                logger.info('Hubitat response is %s' % resp.status_code)
            except Exception as e:
                if hasattr(e, 'message'):
                    # logger.error('Failed to send data to Hubitat - ' + e.message)
                    logger.error(e)
                else:
                    logger.error('Failed to send data to Hubitat')
                    logger.error(e)
            # And send to INflux
            json_body = [
                {
                    "measurement": session,
                        "tags": {
                            "run": runNo,
                            "sensor":2
                            },
                        #"time": iso,
                        "fields": {
                            "liters" : liters,
                            "pulses" : f
                        }
                    }
                ]
            try:
                logger.debug('Sending FLOW to Corlysis Influx - ' + str(json_body))
                corlysisClient.write_points(json_body)
            except Exception as e:
                logger.error('Failed to send data to Corlysis InfluxDB')
                if hasattr(e, 'message'):
                    logger.error(e.message)
                else:
                    logger.debug(e)
            logger.info('End of logging run going to sleep')
            time.sleep(self.INTERVAL_SECONDS)

    def start(self):
        logger.info('Start Processing')
        self._timer_loop()

sh = SampleHandler()
sh.start()

