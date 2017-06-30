# Script to test the bindings of the Logitech Gamepad 310 buttons
# Prints the name of the pushed button/joystick/..

from evdev import InputDevice, categorize, ecodes, KeyEvent, InputEvent

game_pad = InputDevice("/dev/input/event16")

for event in game_pad.read_loop():
    key_event = categorize(event)
    if event.type == ecodes.EV_KEY:
        #print key_event
        if key_event.keystate == KeyEvent.key_down:
            scan_code = key_event.scancode
            print "hi"
            if scan_code == 304:  # A
                print "Back"
            elif scan_code == 308:  # Y
                print "Forward"
            elif scan_code == 305:  # B
                print "Right"
            elif scan_code == 307:  # X
                print "Left"
            elif scan_code == 311:  # R1
                print "R1"
            elif scan_code == 310:  # L1
                print "L1"
            elif scan_code == 314:  # Back
                print "Back"
            elif scan_code == 315:  # Start
                print "Start"

    if event.type == ecodes.EV_ABS:
        event_code = key_event.event.code
        if event_code == 2:
            print "ABS_Z L2"
        elif event_code == 5:
            print "ABS_RZ R2"
        elif event_code == 0:
            print "ABS_X left/right"
        elif event_code == 1:
            print "ABS_Y up/down"
        elif event_code == 3:
            print "ABS_RX left/right"
        elif event_code == 4:
            print "ABS_RX up/down"
        elif event_code == 16:
            print "ABS_HAT0X left/right"
        elif event_code == 17:
            print "ABS_HAT0Y up/down"

