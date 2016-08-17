import datetime
import time
import logging
import sys


class BuzzerEvent:
    power_pin = 23

    def __init__(self, start='2015-12-31 06:30:00', end='0', name='Untitled', duration=1):
        self.name = name
        self.duration = duration
        self.start = start
        self.end = end

    def toggle(self):
        try:
            logging.info("Buzzer - \"" + self.name + "\" - ON - " + str(datetime.datetime.now()) + " - Power pin " +
                         str(self.power_pin) + " (Duration: " + str(self.duration) + " seconds)")
            time.sleep(self.duration)
            logging.info("Buzzer - \"" + self.name + "\" - OFF - " + str(datetime.datetime.now()) + " - Power pin " +
                         str(self.power_pin))
        except:
            logging.critical("Unexpected error:", sys.exc_info()[0])
