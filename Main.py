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

buzzers = []
for job in config['daily']:
    b = NormalBuzzer.NormalBuzzer(name=job['name'],
                                  time=job['time'],
                                  duration=job['buzzer_duration_secs'],
                                  pwr_pin=config["power_pin"])
    buzzers.append(b)
logging.info("Daily scheduled jobs loaded into memory! (Total: %s)", str(len(buzzers)))

special_buzzers = []
for job in config['special']:
    b = SpecialBuzzer.SpecialBuzzer(name=job['name'],
                                    run_date=job['run_date'],
                                    duration=job['buzzer_duration_secs'],
                                    pwr_pin=config["power_pin"])
    special_buzzers.append(b)
logging.info("Special scheduled jobs loaded into memory! (Total: %s)", str(len(special_buzzers)))

scheduler = BlockingScheduler()
for bt in buzzers:
    run_time = bt.time.split(":")
    scheduler.add_job(bt.toggle,
                      'cron',
                      name=bt.name,
                      day_of_week='mon-sun',
                      hour=int(run_time[0]),
                      minute=int(run_time[1]))

# Set up special occasion schedule
for so in special_buzzers:
    scheduler.add_job(so.toggle, 'date', id=bt.name.replace(" ", "-"), name=bt.name, run_date=so.run_date)

# Begin Schedule
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    logging.debug("Keyboard Interruption or System Exit!")
    pass
