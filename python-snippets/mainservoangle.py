from machine import *
p4=Pin(04,Pin.OUT)

p=PWM(p4)
p.freq(50)

import time



def angle(deg):
    y=120-21
    
    x=y/180
    finaldeg=x*deg
    p.duty(round(21+finaldeg))
angle(0)

while True:
    inp=int((input('enter angle in degrees: ')))
    angle(inp)
    time.sleep(5)
    p.duty(angle(0))
    if inp=='e' or inp=='E':
        break