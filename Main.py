import schedule
import time
import BuzzerDummy
import json
import logging

# Set up logger
log_format = '[%(levelname)s] - %(message)s'
logging.basicConfig(filename='example.log', format=log_format, level=logging.DEBUG)

# Read in the config file
with open('config.json', 'r') as f:
    config = json.load(f)
logging.info("config.json file loaded!")

# Load in Buzzer Tasks from config
buzzers = []
for task in config['tasks']:
    b = BuzzerDummy.BuzzerDummy(name=task['name'],
                                time=task['time'],
                                duration=task['buzzer_duration_secs'],
                                pwr_pin=config["power_pin"])
    buzzers.append(b)
logging.info("Tasks loaded into memory! (Total: %s)", str(len(buzzers)))

# Set up the schedule
for bt in buzzers:
    schedule.every().day.at(bt.time).do(bt.toggle)
logging.info("Buzzer tasks loaded into scheduler!")

logging.info("Starting schedule listener...")
logging.info("Next scheduled task is at %s", schedule.next_run())
# Begin Schedule Loop
while True:
    schedule.run_pending()
    time.sleep(1)
