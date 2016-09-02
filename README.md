# Buzzer System

This program was designed to be used to power a buzzer system in a facility. This package assumes a lot of things about the hardware setup.

## Hardware Requirements

- Raspberry Pi (RPi3 Recommended)
- [PowerSwitch Tail II](https://www.adafruit.com/product/268)
- Leads required to connect Rpi and PowerSwitch Tail II together.

## Software Requirements
- Python 3

## Installing Requirements
This project assumes that you already have a distribution of linux on your RPi.

Open the terminal and change the directory to the root of this project (where the requirements.txt file is)

Execute the following command:
`sudo -H pip install -r requirements.txt`

This should install all the third party software required for the project.

## Setting up the hardware
Using you leads you will need to connect the RPi to the PowerSwitch Tail II.

This project uses the [BCM pin setup](http://i.stack.imgur.com/sVvsB.jpg). (You will likely need to lookup the diagram for this if this URL does not work).

The left side of the table below is the pin on the Raspberry Pi and the right side of the table is the destination slot on the PowerSwitch Tail II.

| RPi Pin Location 	| PowerSwitch Tail II 	|
|------------------	|---------------------	|
| Pin #16 (GPIO23) 	| 1. +IN              	|
| Pin #14 (Ground) 	| 2. -IN              	|

Be sure to set this up correctly. Incorrect setup for cause damage to your hardware or could just simply not work.

## Configuration
There are two styles of buzzers available in the `config.json`:

`Daily` - These are scheduled to run every day.
`special` - These are scheduled to run at the specfied start time and also an end time if specified.

##### Daily's Properties
- `name` This is a required friendly name for the buzzer object
- `start` The time in which the buzzer should be activated. The date is ignore but still needs to be set. Its recommended to make it '9999-12-31' for clarity purposes. Time is in 24-Hour format.
- `duration_secs` The duration in which the power is allowed through the PowerSwitch Tail II in seconds.

##### Special's Properties
- `name` This is a required friendly name for the buzzer object
- `start` The time in which the buzzer should be activated. The date is ignore but still needs to be set. Its recommended to make it '9999-12-31' for clarity purposes. Time is in 24-Hour format.
- `end` *(optional)* The time in which the buzzer should be ran again to signify the end of this special buzzer.
- `duration_secs` The duration in which the power is allowed through the PowerSwitch Tail II in seconds.

## Execution
To execute the program, simply navigate to the root of the project in the terminal window and run the following command:

`python3 Main.py`

==Be sure that you have run the requirements code before you attempt to run the project for the first time.==

- - -

## License
MIT Licenses

Copyright (c) [2016] [[Joshua C Garrison](http://joshuacgarrison.com)]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
