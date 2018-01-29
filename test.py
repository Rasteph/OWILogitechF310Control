import inputCheck

iCheck = inputCheck.inputCheck()

devicename = raw_input('Enter a file name: ')

print 'Input event number of wanted device:'
iCheck.printFnumber(devicename)

print 'All input devices with input event number, name and physical address'
iCheck.printInputDevices()