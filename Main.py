import schedule
import time
import BuzzerDummy
import json

# Read in the config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Load in Buzzer Tasks from config
buzzers = []
for task in config['tasks']:
    b = BuzzerDummy.BuzzerDummy(name=task['name'], time=task['time'], duration=task['buzzer_duration_secs'])
    buzzers.append(b)

# Set up the schedule
for bt in buzzers:
    schedule.every().day.at(bt.time).do(bt.toggle)

# Begin Schedule Loop
while True:
    schedule.run_pending()
    time.sleep(1)
