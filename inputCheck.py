import evdev
found = False
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()] 

class inputCheck:    
    def __init__(self):
        self.devices = devices

    def printInputDevices(self):
        print evdev.list_devices() 
        for device in self.devices:
            print (device.fn, device.name, device.phys)
            return device.name

    def printFnumber(self, device_name):
        for device in self.devices:
            if device.name == device_name:
                return device.fn
            else:
                print 'Device not found.'