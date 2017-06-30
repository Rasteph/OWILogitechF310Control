OWO Robotic Arm controlled by a Logitech F310 Gamepad

Used devices:
 - OWO Robotic Arm
 - USB control board (OWO toy robot arm accessory)
 - Logitech F310 Gamepad
 - Linux machine (laptop, raspberry pi, ...)

The Logitech F310 gamepad as well as the OWO Robotic Arm USB control board are connected to a linux machine which handles the communication between both devices.

This approach is based on http://mattdyson.org/projects/robotarm/ (Xbox 360 Wireless Controller for Windows + Raspi).
Matt Dysons approach uses the lego-pi library (https://github.com/zephod/lego-pi) which reads event objects from the Xbox controller, and updates the GPIO/I2C outputs on the Raspberry Pi as appropriate. 
The lego-pi library does not work with the Logitech F310 Gamepad (as far as i know, without sophisticated adjustments to the library).

To read and interpret the events (e.g. Button X pushed) of the Logitech F310 Gamepad, the OWOLogitechF310Control uses these additional libraries:
- evdev - A generic Linux input driver https://linux.die.net/man/4/evdev
- pyusb - USB devices communication in Python https://pypi.python.org/pypi/pyusb/1.0.0

This repository includes the needed python scripts to control the popular OWO toy robot arm with a Logitech F310 gamepad.
The scripts provided by Matt Dyson:
  - RobotArm.py
  - testRobotArm.py
Scripts provided by me:
  - controlRobotArm.py:
    - contains the logic on which buttons control which robot arm movement
    - input device needs to be set in this script (e.g. "/dev/input/event16")
  - gamePadTest.py:
    - elaborates on the bindings of the Logitech Gamepad 310 buttons and prints the name of the pushed button/joystick/..
    - input device needs to be set in this script (e.g. "/dev/input/event16")
  - joyInfo.py
  
 What needs to be started to use the Logitech F310 Gampepad as controller:
  1. run RobotArm.py
  2. run controlRobotArm.py
  3. push desired button ;)
  
  
  
