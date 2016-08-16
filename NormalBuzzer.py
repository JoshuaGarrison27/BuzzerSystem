import datetime
import time
import logging
import sys


class NormalBuzzer:
    def __init__(self, time='09:00', name='Untitled', duration=1, pwr_pin=23):
        self.name = name
        self.duration = duration
        self.power_pin = pwr_pin
        self.time = time

    def toggle(self):
        try:
            logging.info("Buzzer - \"" + self.name + "\" - ON - " + str(datetime.datetime.now()) + " - Power pin " +
                         str(self.power_pin) + " (Duration: " + str(self.duration) + " seconds)")
            time.sleep(self.duration)
            logging.info("Buzzer - \"" + self.name + "\" - OFF - " + str(datetime.datetime.now()) + " - Power pin " +
                         str(self.power_pin))
        except:
            logging.critical("Unexpected error:", sys.exc_info()[0])
