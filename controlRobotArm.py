# Script containing logic on which buttons and controls trigger what OWI robotic arm motion.
#
#
# config: R2:                       moveBase ->
#         L2:                       moveBase <-
#         right joystick upwards:   moveShoulder ^
#         right joystick downwards: moveShoulder v
#         left joystick upwards:    moveElbow ^
#         left joystick downwards:  moveElbow v
#         arrow top:                moveWrist ^
#         arrow down:               moveWrist v
#         R1 moveGrip:              open
#         L1 moveGrip:              close

import RobotArm
import inputCheck
from evdev import InputDevice, categorize, ecodes, KeyEvent, InputEvent

arm = RobotArm.RobotArm()
# input event depends on the device in use
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
    print game_pad.active_keys(True)
    if len(game_pad.active_keys()) < 1 and lastKey == 1: # only move gripper if L1/R1 pushed
        arm.reset()
    elif event.type == ecodes.EV_KEY and key_event.keystate == KeyEvent.key_down:
        scan_code = key_event.scancode
        if scan_code == 311:  # R1
            print "R1"
            arm.moveGrip(1)
            lastKey = 1
        elif scan_code == 310:  # L1
            print "L1"
            arm.moveGrip(2)
            lastKey = 1
        # elif scan_code == 314:  # Back
        #     print "Back"
        # elif scan_code == 315:  # Start
        #     print "Start"
        # elif scan_code == 308:  # Y
        #     print "Forward"
        # elif scan_code == 305:  # B
        #     print "Right"
        # elif scan_code == 307:  # X
        #     print "Left"
        # elif scan_code == 304:  # A
        #     print "Back"

    if event.type == ecodes.EV_ABS:
        lastKey = 0
        event_code = key_event.event.code
        # moveBase
        if event_code == 2:
            print "ABS_Z L2"
            if event.value > 0:
                arm.moveBase(1)
            else:
                arm.moveBase(0)
        elif event_code == 5:
            print "ABS_RZ R2"
            if event.value > 0:
                arm.moveBase(2)
            else:
                arm.moveBase(0)

        # moveElbow
        elif event_code == 0:
            print "ABS_X left/right"
            if -1000 < event.value < 1000:
                arm.moveElbow(0)
            elif event.value > 1000:
                arm.moveElbow(1)
            elif event.value < -1000:
                arm.moveElbow(2)

        # moveShoulder
        elif event_code == 3:
            print "ABS_RX left/right"
            if -1000 < event.value < 1000:
                arm.moveShoulder(0)
            elif event.value > 1000:
                arm.moveShoulder(1)
            elif event.value < -1000:
                arm.moveShoulder(2)

        # moveGrip
        elif event_code == 16:
            print "ABS_HAT0X left/right"
            if -1000 < event.value < 1000:
                arm.moveGrip(0)
            elif event.value > 1000:
                arm.moveGrip(1)
            elif event.value < -1000:
                arm.moveGrip(2)

