from apscheduler.schedulers.blocking import BlockingScheduler
import BuzzerEvent
import json
import logging
import datetime
import sys
import RPi.GPIO as io

# Set up logger
log_format = '[%(levelname)s] [%(asctime)s] - %(message)s'
logging.basicConfig(filename='Activity.log', level=logging.DEBUG)
logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')

# Set up system print out for end user
root = logging.getLogger()
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
root.addHandler(ch)

logging.info("=========== Gastonia Buzzer System ===========")

# Set up RPi GPIO
# io.BCM says use the BCM GPIO numbering system for pins.
io.setmode(io.BCM)
io.setup(23, io.OUT)

# Read in the config file
with open('config.json', 'r') as f:
    config = json.load(f)
logging.info("config.json file loaded!")

# Load in daily buzzer tasks from config
buzzers = []
for job in config['daily']:
    start_time = datetime.datetime.strptime(job['start'], "%Y-%m-%d %H:%M:%S")
    b = BuzzerEvent.BuzzerEvent(name=job['name'],
                                start=str(start_time.hour) + ":" + str(start_time.minute),
                                duration=job['duration_secs'])
    buzzers.append(b)
logging.info("Daily scheduled jobs loaded into memory! (Total: %s)", str(len(buzzers)))

# Load in special buzzer tasks from config
special_buzzers = []
for job in config['special']:
    b = BuzzerEvent.BuzzerEvent(name=job['name'],
                                start=job['start'],
                                duration=job['duration_secs'])
    if job['end'] is not None:
        b.end = job['end']
    special_buzzers.append(b)
logging.info("Special scheduled jobs loaded into memory! (Total: %s)", str(len(special_buzzers)))

# Set up the daily schedule
scheduler = BlockingScheduler()
for bt in buzzers:
    run_time = bt.start.split(":")
    scheduler.add_job(bt.toggle,
                      'cron',
                      name=bt.name.replace(" ", "-"),
                      day_of_week='mon-sun',
                      hour=int(run_time[0]),
                      minute=int(run_time[1]))

# Set up special occasion schedule
for so in special_buzzers:
    scheduler.add_job(so.toggle, 'date',  name=so.name, run_date=so.start)
    if so.end is not None:
        scheduler.add_job(so.toggle, 'date',  name=so.name+'-end', run_date=so.end)

# Start Schedule
try:
    print("Config Complete!")
    print("Starting Scheduler...")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    logging.debug("Keyboard Interruption or System Exit! Program halting...")
    print("Keyboard Interruption or System Exit! Program halting...")
finally:
    io.cleanup()
