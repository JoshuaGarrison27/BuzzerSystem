from apscheduler.schedulers.blocking import BlockingScheduler
import NormalBuzzer
import SpecialBuzzer
import json
import logging

# Set up logger
log_format = '[%(levelname)s] - %(message)s'
logging.basicConfig(filename='Activity.log', format=log_format, level=logging.DEBUG)

logging.info("=========== Gastonia Buzzer System ===========")

# Read in the config file
with open('config.json', 'r') as f:
    config = json.load(f)
logging.info("config.json file loaded!")

# Load in daily buzzer tasks from config
buzzers = []
for job in config['daily']:
    b = NormalBuzzer.NormalBuzzer(name=job['name'],
                                  time=job['time'],
                                  duration=job['buzzer_duration_secs'],
                                  pwr_pin=config["power_pin"])
    buzzers.append(b)
logging.info("Daily scheduled jobs loaded into memory! (Total: %s)", str(len(buzzers)))

# Load in special buzzer tasks from config
special_buzzers = []
for job in config['special']:
    b = SpecialBuzzer.SpecialBuzzer(name=job['name'],
                                    start_buzzer=job['start_buzzer'],
                                    duration=job['buzzer_duration_secs'],
                                    pwr_pin=config["power_pin"])
    if job['end_buzzer'] is not '0':
        b.end_buzzer = job['end_buzzer']
    special_buzzers.append(b)
logging.info("Special scheduled jobs loaded into memory! (Total: %s)", str(len(special_buzzers)))

# Set up the daily schedule
scheduler = BlockingScheduler()
for bt in buzzers:
    run_time = bt.time.split(":")
    scheduler.add_job(bt.toggle,
                      'cron',
                      name=bt.name.replace(" ", "-"),
                      day_of_week='mon-sun',
                      hour=int(run_time[0]),
                      minute=int(run_time[1]))

# Set up special occasion schedule
for so in special_buzzers:
    scheduler.add_job(so.toggle, 'date',  name=so.name, run_date=so.start_buzzer)
    if so.end_buzzer is not '0':
        scheduler.add_job(so.toggle, 'date',  name=so.name+'-end', run_date=so.end_buzzer)

# Begin Schedule
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    logging.debug("Keyboard Interruption or System Exit!")
    pass
