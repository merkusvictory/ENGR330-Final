from microbit import *

def stopBit(color):
    if color == "green":
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
    elif color == "amber":
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif color == "red":
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
