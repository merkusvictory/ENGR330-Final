from microbit import *

def arrow_point(X, Y):
    if X == 0:
        pin0.write_analog(80)
    elif Y == 'E':
        pin0.write_analog(30)
    elif (X == 1 and Y == 'D') or (X == 2 and Y == 'C') or (X == 3 and Y == 'B') or (X == 4 and Y == 'A'):
        pin0.write_analog(55)
    elif (X == 2 and Y == 'D') or (X == 3 and Y == 'C') or (X == 4 and Y == 'B'):
        pin0.write_analog(47)
    elif (X == 3 and Y == 'D') or (X == 4 and Y == 'C'):
        pin0.write_analog(78)
    elif (X == 4 and Y == 'D'):
        pin0.write_analog(34)
    elif (X == 1 and Y == 'C') or (X == 2 and Y == 'B') or (X == 3 and Y == 'A'):
        pin0.write_analog(64)
    elif (X == 2 and Y == 'A') or (X == 1 and Y == 'B'):
        pin0.write_analog(72)
    elif (X == 1 and Y == 'A'):
        pin0.write_analog(78)
    else:
        pin0.write_analog(0)
