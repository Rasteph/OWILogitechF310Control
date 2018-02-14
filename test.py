import inputCheck

iCheck = inputCheck.inputCheck()


if not iCheck.devices:
    print 'no devices found'
else:
    devicename = raw_input('Enter the device name: ')
    print 'Input event number of wanted device:'
    iCheck.printFnumber(devicename)
    print 'All input devices with input event number, name and physical address'
    iCheck.printInputDevices()