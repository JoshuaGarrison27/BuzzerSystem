import datetime
import time
from threading import Thread


class BuzzerDummy:

    def __init__(self, time='09:00', name='Untitled', duration=1, pwr_pin=23):
        self.name = name
        self.duration = duration
        self.time = time
        self.power_pin = pwr_pin

    def toggle(self):
        print("Buzzer - \"" + self.name + "\" - ON - " + str(datetime.datetime.now()) + " - Power pin " + str(
            self.power_pin) + " (Duration: " + str(self.duration) + " seconds)")
        time.sleep(self.duration)
        print("Buzzer - \"" + self.name + "\" - OFF - " + str(datetime.datetime.now()) + " - Power pin " + str(
            self.power_pin))
        print("____________________________________________________________________")

    def trigger_buzzer(self):
        t = Thread(target=self.toggle())
        t.start()
