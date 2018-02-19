# Script containing logic on buttons and controls triggering OWI robotic arm motion.
# Gamepad events of the Logitech Gamepad F310 trigger motion of OWI robotic arm motors and the light bulb.
#
# config: R2:                           moveBase ->
#         L2:                           moveBase <-
#         right joystick rightwards:    moveShoulder ^
#         right joystick leftwards:     moveShoulder v
#         left joystick rightwards:     moveElbow ^
#         left joystick leftwards:      moveElbow v
#         arrow right:                  moveWrist ^
#         arrow left:                   moveWrist v
#         R1 moveGrip:                  open
#         L1 moveGrip:                  close
#
# Information on Logitech Gamepad F310: https://www.logitech.com/assets/35017/gamepad-f310-gsw.pdf

import OWIRoboticArmController
import inputCheck
from evdev import InputDevice, categorize, ecodes, KeyEvent, InputEvent

OWIarm = OWIRoboticArmController.OWIRoboticArm()

# grabs input device associated to game pad label
# check with $ ls /dev/input/
iCheck = inputCheck.inputCheck()
gamepadEvent = iCheck.printFnumber("Logitech Gamepad F310")
game_pad = InputDevice(str(gamepadEvent))
print "Input device Logitech Gamepad F310 ready to use."
#game_pad = InputDevice("/dev/input/event16")

game_pad.capabilities()
game_pad.capabilities(verbose=False)
lastKey = 0 # 1 == L1 or R1, 0 == other keys 

for event in game_pad.read_loop():
    key_event = categorize(event)
    #print game_pad.active_keys(True)
    if len(game_pad.active_keys()) < 1 and lastKey == 1: # only move gripper if L1/R1 pushed
        switchLight = False
        OWIarm.stopMotion(switchLight)

    # Trigger for:
    # Right/left button trigger, Y action button
    elif event.type == ecodes.EV_KEY and key_event.keystate == KeyEvent.key_down:
        scan_code = key_event.scancode
        if scan_code == 311:  # R1
            #print "R1"
            OWIarm.gripMotion(1)
            lastKey = 1
        elif scan_code == 310:  # L1
            #print "L1"
            OWIarm.gripMotion(2)
            lastKey = 1
        
        elif scan_code == 308 and KeyEvent.key_down: # Y
            #print "Y"
            lastKey = 0
            switch = OWIarm.getLightSwitch()
            if switch == 0:
                switch = 1
            elif switch ==1:
                switch = 0
            OWIarm.setLightSwitch(switch)

    # Trigger for:
    # analog-sticks, D-Pad, RT, LT
    if event.type == ecodes.EV_ABS:
        lastKey = 0
        event_code = key_event.event.code
        # moveBase
        if event_code == 2:
            #print "ABS_Z L2"
            if event.value > 0:
                OWIarm.baseMotion(1)
            else:
                OWIarm.baseMotion(0)
        elif event_code == 5:
            #print "ABS_RZ R2"
            if event.value > 0:
                OWIarm.baseMotion(2)
            else:
                OWIarm.baseMotion(0)

        # moveElbow
        elif event_code == 0:
            #print "ABS_X left/right"
            if -1000 < event.value < 1000:
                OWIarm.elbowMotion(0)
            elif event.value > 1000:
                OWIarm.elbowMotion(1)
            elif event.value < -1000:
                OWIarm.elbowMotion(2)

        # moveShoulder
        elif event_code == 3:
            #print "ABS_RX left/right"
            if -1000 < event.value < 1000:
                OWIarm.shoulderMotion(0)
            elif event.value > 1000:
                OWIarm.shoulderMotion(1)
            elif event.value < -1000:
                OWIarm.shoulderMotion(2)

        elif event_code == 17:
            #print "ABS_HAT0Y left/right"
            if event.value > 0:
                OWIarm.wristMotion(2)
            elif event.value < 0:
                OWIarm.wristMotion(1)
            else:
                OWIarm.wristMotion(0)


