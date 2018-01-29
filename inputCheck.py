import evdev
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
found = False

class inputCheck:

    #def __init__(self):
    
    def printInputDevices(self):
        print evdev.list_devices() 
        for device in devices:
            print (device.fn, device.name, device.phys)

    def printFnumber(self, device_name):
        for device in devices:
            if device.name == device_name:
                print device.fn
            else:
                print 'Device not found.'