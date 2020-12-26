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
import requests

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
# client = InfluxDBClient(host, port, user, password, dbname,False,False,3)
corlysisClient = InfluxDBClient(host='corlysis.com', port=port, username='token',password='48abd1cc8081ae4bdd109e170c047040',
    database='pond',ssl=True,verify_ssl=False,timeout=15,retries=3)
print ("Session: ", session)
print ("runNo: ", runNo)

logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,
                    format='{%(asctime)s}[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
logger = logging.getLogger('my_logger')
logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG,
                    format='{%(asctime)s}[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
handler = RotatingFileHandler('./logs/PondTemp.log', maxBytes=10000, backupCount=10)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

''' Temperature sensor wrapper. Gets temperature readings from file.
'''
class TempSensor(object):
    def __init__(self, a_file_name):
        if len(a_file_name) > 0:
            self.file_name = a_file_name
        else:
            self.file_name = None
        self.last_good_temp = 0.0

    def get_temp(self):
        if self.file_name is None:
            return self.last_good_temp
        with open(self.file_name) as f:
            content = f.readlines()
            for line in content:
                # sometimes CRC is bad, so we will return last known good temp
                if line.find('crc=') >= 0 and line.find('NO') >= 0:
                    logger.warn('Bad read on sensor')
                    return self.last_good_temp
                p = line.find('t=')
                if p >= 0:
                    self.last_good_temp = float(line[p+2:]) / 1000.0
                    return self.last_good_temp
        return self.last_good_temp

class SampleHandler():
    INTERVAL_SECONDS = 60
    def __init__(self):
        self._sensors = []
        files = glob.glob('/sys/bus/w1/devices/28-*/w1_slave')
        for f in files:
            self._sensors.append(TempSensor(f))
        self._scheduler = sched.scheduler(time.time, time.sleep)

    def _timer_loop(self):
        hURL ='http://192.168.2.106/apps/api/417/devices/'
        while True:
            logger.info('Start logging run')
            for index,s in enumerate(self._sensors):
                t = s.get_temp()
                # 0.5 degree calibration factor
                tF = t * 1.8 + 32 + 0.5
                hIdxURL = hURL + '612' + '/setTemperature/' + str(tF) + '?access_token=c82410cc-4e3b-4eb2-8055-bf3ff4e55678'
                logger.debug('Send to Hubitat - ' + hIdxURL)
                resp = requests.get(hIdxURL, timeout=3)
                logger.info('Hubitat response is %s' % resp.status_code)
                # And send to Influx
                json_body = [
                    {
                    "measurement": session,
                        "tags": {
                            "run": runNo,
                            "sensor":2
                            },
                        #"time": iso,
                        "fields": {
                            "temperature" : tF,
                        }
                    }
                ]
            try:
                logger.debug('Sending to Corlysis Influx - ' + str(json_body))
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
        logger.debug('Start Processing')
        self._timer_loop()

sh = SampleHandler()
sh.start()


# %%
