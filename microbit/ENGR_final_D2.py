from microbit import *
import radio
from arrow_point import *
from location_graph import *

radio.on()
radio.config(channel=17)

time = 0

uart.init(baudrate=115200)
display.show(Image.ASLEEP)

pin0.set_analog_period(20)

valueA = None
valueB = None
valueC = None

while True:
    # Read radio messages
    message = radio.receive()
    if message is not None:
        # print(str(message))
        var = message.split(',')

        if var[0] == 'A':
            valueA = str(var[1])
        if var[0] == 'B':
            valueB = str(var[1])
        if var[0] == 'C':
            valueC = str(var[1])

        # Send values to model
        time += 100
        sleep(100)

        if time % 300 == 0:
            if (valueA is not None) and (valueB is not None) and (valueC is not None):
                print(valueA + ',' + valueB + ',' + valueC)

    if uart.any():
        msg_bytes = uart.read()
        msg = msg_bytes.decode('utf-8').strip()
        radio.send(msg)
        keys = msg.split(',')
        loc_graph(int(keys[0]), keys[1])
        arrow_point(int(keys[0]), keys[1])
        sleep(100)

