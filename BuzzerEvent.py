import datetime
import time
import logging
import sys
import RPi.GPIO as io


class BuzzerEvent:
    def __init__(self, start='2015-12-31 06:30:00', end='0', name='Untitled', duration=1):
        self.name = name
        self.duration = duration
        self.start = start
        self.end = end

    def toggle(self):
        try:
            # Turn On Buzzer
            io.output(23, True)
            logging.info("Buzzer - \"" + self.name + "\" - ON - " + str(datetime.datetime.now()) + " (Duration: " + str(self.duration) + " seconds)")

            # Wait for duration of the buzzer requested
            time.sleep(self.duration)

            # Turn Off Buzzer
            io.output(23, False)
            logging.info("Buzzer - \"" + self.name + "\" - OFF - " + str(datetime.datetime.now()))
        except:
            logging.critical("Unexpected error:", sys.exc_info()[0])
