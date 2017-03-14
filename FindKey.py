from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event16')
for event in gamepad.read_loop():
    key_event = categorize(event)
    # print keyevent.event.code
    print key_event
    print "value", event.value
    # print keyevent

    if event.type == ecodes.FF:
        print("FF2")

