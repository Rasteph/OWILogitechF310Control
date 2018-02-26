## OWI Robotic Arm controlled by the Logitech F310 Gamepad

[Click to watch youtube video. <img src="https://github.com/pastelhh/OWILogitechF310Control/blob/master/img/OWILogitechGamepadF310.jpg?raw=true" width="480">](https://www.youtube.com/watch?v=YJlikTFGr-c&feature=youtu.be "OWI Robotic arm controlled by Logitech Gamepad F310 - Click to Watch!")

Used devices:
 - OWI Robotic Arm
 - USB control board (OWI toy robot arm accessory)
 - Logitech F310 Gamepad
 - Linux machine (laptop, raspberry pi, ...)

The Logitech F310 gamepad as well as the OWI Robotic Arm USB control board are connected to a linux machine which handles the communication between both devices.


This approach is based on http://mattdyson.org/projects/robotarm/ (Xbox 360 Wireless Controller for Windows + Raspi).
Matt Dysons approach uses the lego-pi library (https://github.com/zephod/lego-pi) which reads event objects from the Xbox controller, and updates the GPIO/I2C outputs on the Raspberry Pi as appropriate. 
The lego-pi library does not work with the Logitech F310 Gamepad (as far as i know, without sophisticated adjustments to the library).

To read and interpret the events (e.g. Button X pushed) of the Logitech F310 Gamepad, the OWILogitechF310Control uses these additional libraries:
- evdev - A generic Linux input driver https://linux.die.net/man/4/evdev
- pyusb - USB devices communication in Python https://pypi.python.org/pypi/pyusb/1.0.0

Python package:
- **OWIRoboticArmController.py** : Class to control the OWI Robotic Arm via USB
- **controlOWIRoboticArm.py**    : Script containing logic on buttons and controls triggering the OWI Robotic Arm motions
- **gamePadTest.py**             : Names the labels of the pushed buttons and controls on the Logitech Gamepad F310
- **inputCheck.py**              : Helper class providing information on connected input devices on the linux machine
- **test.py**                    : Names the input event number of a wanted input device and other connected devices

 ### What needs to be started to use the Logitech F310 Gampepad as controller for the OWI Robotic Arm:
  1. Clone GitHub project
  2. Make `controlOWIRoboticArm.py` executable 
  3. Connect Logitech Gamepad F310 and OWI Robotic Arm to the Linux machine
  4. run `sudo python contrlOWIRoboticArm.py`
  5. push buttons on the gamepad ;)

