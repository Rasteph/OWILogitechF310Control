# Class to control the OWI Robotic Arm.
# Each motor and the light bulb of the OWI Robtic Arm are accessed via USB.
#
# Inspired by   http://mattdyson.org/projects/robotarm
# and           http://notbrainsurgery.livejournal.com/38622.html

import usb.core as usbdev
import time

vendor = 0x1267
product = 0x0000
timeout = 1000

class OWIRoboticArm:

    def __init__(self):
        # Connection to OWI Robotic Arm is established
        self.OWIArmUsbDevice = usbdev.find(idVendor=vendor, idProduct=product)
        if not self.OWIArmUsbDevice:
            raise ValueError("Could not connect to OWI Robotic Arm.")
        self.OWIArmUsbDevice.set_configuration()

        # Initialize motors and light bulb to be in idle/resting state
        self.stopMotion()

    def __del__(self):
        self.stopMotion()

    # Send latest command/data to OWI Robotic Arm via USB control transfer
    def sendCommand(self):
        cmd = self.setupCommand()
        self.OWIArmUsbDevice.ctrl_transfer(0x40, 6, 0x100, 0, cmd, timeout)

    # Setup data field for USB control transfer
    def setupCommand(self):
        bytes = [0] * 3
        bytes[0] = (self.shoulder << 6) + (self.elbow << 4) + (self.wrist << 2) + self.grip
        bytes[1] = self.base
        bytes[2] = self.lightSwitch
        return bytes

    def stopMotion(self, switchLight = True):
        self.base = 0
        self.elbow = 0
        self.grip = 0
        if switchLight:
            self.lightSwitch = 0
        self.shoulder = 0
        self.wrist = 0
        self.sendCommand()

    # set motion directions for the motors
    def baseMotion(self, motionDirection):
        self.base = motionDirection
        self.sendCommand()
    
    def shoulderMotion(self, motionDirection):
        self.shoulder = motionDirection
        self.sendCommand()

    def elbowMotion(self, motionDirection):
        self.elbow = motionDirection
        self.sendCommand()

    def wristMotion(self, motionDirection):
        self.wrist = motionDirection
        self.sendCommand()

    def gripMotion(self, motionDirection):
        self.grip = motionDirection
        self.sendCommand()

    # set light switch
    # 0: light off
    # 1: light on
    def setLightSwitch(self, switch):
        self.lightSwitch = switch
        self.sendCommand()

    def getLightSwitch(self):
        return self.lightSwitch
