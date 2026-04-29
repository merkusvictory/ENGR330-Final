from microbit import *
import radio
from stopbit import *
from location_graph import *

radio.on()
radio.config(channel=17)

while True:
    # read and send sound level
    sound = microphone.sound_level()
    radio.send("B," + str(sound))
    print("B," + str(sound))
    # display.show(sound)
    sleep(100)
    radio.send("None")

    # lights
    if sound > 5:
        stopBit("green")
    elif sound > 1:
        stopBit("amber")
    else:
        stopBit("red")

    # get location info and show
    msg = radio.receive()
    if msg is not None:
        keys = msg.split(',')
        try:
            if int(keys[0]) >= 0:
                loc_graph(int(keys[0]), keys[1])
            msg = None
        except:
            pass
