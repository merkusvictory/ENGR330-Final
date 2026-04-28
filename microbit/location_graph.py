from microbit import *

spot_a = Image("0:" "0:" "0:" "0:" "9:")
spot_b = Image("0:" "0:" "0:" "0:" "09:")
spot_c = Image("0:" "0:" "0:" "0:" "009:")
spot_d = Image("0:" "0:" "0:" "0:" "0009:")
spot_e = Image("0:" "0:" "0:" "0:" "00009:")
spot_f = Image("0:" "0:" "0:" "9:" "0:")
spot_g = Image("0:" "0:" "0:" "09:" "0:")
spot_h = Image("0:" "0:" "0:" "009:" "0:")
spot_i = Image("0:" "0:" "0:" "0009:" "0:")
spot_j = Image("0:" "0:" "0:" "00009:" "0:")
spot_k = Image("0:" "0:" "9:" "0:" "0:")
spot_l = Image("0:" "0:" "09:" "0:" "0:")
spot_m = Image("0:" "0:" "009:" "0:" "0:")
spot_n = Image("0:" "0:" "0009:" "0:" "0:")
spot_o = Image("0:" "0:" "00009:" "0:" "0:")
spot_p = Image("0:" "9:" "0:" "0:" "0:")
spot_q = Image("0:" "09:" "0:" "0:" "0:")
spot_r = Image("0:" "009:" "0:" "0:" "0:")
spot_s = Image("0:" "0009:" "0:" "0:" "0:")
spot_t = Image("0:" "00009:" "0:" "0:" "0:")
spot_u = Image("9:" "0:" "0:" "0:" "0:")
spot_v = Image("09:" "0:" "0:" "0:" "0:")
spot_w = Image("009:" "0:" "0:" "0:" "0:")
spot_x = Image("0009:" "0:" "0:" "0:" "0:")
spot_y = Image("00009:" "0:" "0:" "0:" "0:")


def loc_graph(X, Y):
    if X == 0:
        if Y == 'A':
            display.show(spot_a)
        elif Y == 'B':
            display.show(spot_b)
        elif Y == 'C':
            display.show(spot_c)
        elif Y == 'D':
            display.show(spot_d)
        elif Y == 'E':
            display.show(spot_e)
    if X == 1:
        if Y == 'A':
            display.show(spot_f)
        elif Y == 'B':
            display.show(spot_g)
        elif Y == 'C':
            display.show(spot_h)
        elif Y == 'D':
            display.show(spot_i)
        elif Y == 'E':
            display.show(spot_j)
    if X == 2:
        if Y == 'A':
            display.show(spot_k)
        elif Y == 'B':
            display.show(spot_l)
        elif Y == 'C':
            display.show(spot_m)
        elif Y == 'D':
            display.show(spot_n)
        elif Y == 'E':
            display.show(spot_o)
    if X == 3:
        if Y == 'A':
            display.show(spot_p)
        elif Y == 'B':
            display.show(spot_q)
        elif Y == 'C':
            display.show(spot_r)
        elif Y == 'D':
            display.show(spot_s)
        elif Y == 'E':
            display.show(spot_t)
    if X == 4:
        if Y == 'A':
            display.show(spot_u)
        elif Y == 'B':
            display.show(spot_v)
        elif Y == 'C':
            display.show(spot_w)
        elif Y == 'D':
            display.show(spot_x)
        elif Y == 'E':
            display.show(spot_y)
