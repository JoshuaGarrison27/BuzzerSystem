import datetime
import time
import logging
import sys


class SpecialBuzzer:
    def __init__(self, start_buzzer='2015-12-31 06:30:00', end_buzzer='0', name='Untitled', duration=1, pwr_pin=23):
        self.name = name
        self.duration = duration
        self.power_pin = pwr_pin
        self.start_buzzer = start_buzzer
        self.end_buzzer = end_buzzer

    def toggle(self):
        try:
            logging.info("Buzzer - \"" + self.name + "\" - ON - " + str(datetime.datetime.now()) + " - Power pin " +
                         str(self.power_pin) + " (Duration: " + str(self.duration) + " seconds)")
            time.sleep(self.duration)
            logging.info("Buzzer - \"" + self.name + "\" - OFF - " + str(datetime.datetime.now()) + " - Power pin " +
                         str(self.power_pin))
        except:
            logging.critical("Unexpected error:", sys.exc_info()[0])
