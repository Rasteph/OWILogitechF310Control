# Class to control the OWI Robotic Arm

import usb.core as usbdev
import time

vendor = 0x1267
product = 0x0000
timeout = 500

class OWIRoboticArm:

    def __init__(self):
        self.OWIArmUsbDevice = usbdev.find(idVendor=vendor, idProduct=product)
        self.OWIArmUsbDevice.set_configuration()
        if not self.OWIArmUsbDevice:
            raise ValueError("Could not connect to OWI Robotic Arm.")
        #self.stopMotion()

    def __del__(self):
        self.stopMotion()

    def sendCommand(self):
        cmd = self.setupCommand()
        self.OWIArmUsbDevice.ctrl_transfer(0x40, 6, 0x100, 0, cmd, timeout)

    def setupCommand(self):
        bytes = [0] * 3
        bytes[0] = (self.shoulder << 6) + (self.elbow << 4) + (self.wrist << 2) + self.grip
        bytes[1] = self.base
        bytes[2] = self.lightSwitch

    def stopMotion(self):
        self.base = 0
        self.elbow = 0
        self.grip = 0
        self.lightSwitch = 0
        self.shoulder = 0
        self.wrist = 0
        self.sendCommand()

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

    def setLightSwitch(self, switch):
        self.lightSwitch = switch
        self.sendCommand()

    def stopMotion(self):
        self.shoulder = 0
        self.elbow = 0
        self.wrist = 0
        self.grip = 0
        self.base = 0
        self.lightSwitch = 0
        self.sendCommand()
