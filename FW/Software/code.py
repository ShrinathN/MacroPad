import random
import time
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode
from lib.adafruit_hid.consumer_control import ConsumerControl
from lib.adafruit_hid.consumer_control_code import ConsumerControlCode
import digitalio
import board
import usb_hid


#keyboard
kbd = Keyboard(usb_hid.devices)
# consumer = ConsumerControl(usb_hid.devices)
# consumer.send(ConsumerControlCode.PLAY_PAUSE)
b0 = digitalio.DigitalInOut(board.GP0)
b0.direction = digitalio.Direction.INPUT
b1 = digitalio.DigitalInOut(board.GP1)
b1.direction = digitalio.Direction.INPUT
b2 = digitalio.DigitalInOut(board.GP2)
b2.direction = digitalio.Direction.INPUT
b3 = digitalio.DigitalInOut(board.GP3)
b3.direction = digitalio.Direction.INPUT
b4 = digitalio.DigitalInOut(board.GP4)
b4.direction = digitalio.Direction.INPUT
b5 = digitalio.DigitalInOut(board.GP5)
b5.direction = digitalio.Direction.INPUT
b6 = digitalio.DigitalInOut(board.GP6)
b6.direction = digitalio.Direction.INPUT
b7 = digitalio.DigitalInOut(board.GP7)
b7.direction = digitalio.Direction.INPUT

r = digitalio.DigitalInOut(board.GP8)
r.direction = digitalio.Direction.OUTPUT
r.value = True
g = digitalio.DigitalInOut(board.GP9)
g.direction = digitalio.Direction.OUTPUT
g.value = True
b = digitalio.DigitalInOut(board.GP10)
b.direction = digitalio.Direction.OUTPUT
b.value = True

def kpr(s):
    kbd.press(s)
    kbd.release(s)


b1_view_changer = True

while(True):
    if(b0.value == False):
        print("b0 pressed")
        kbd.press(Keycode.V)
        kbd.release(Keycode.V)
        kbd.press(Keycode.F)
        kbd.release(Keycode.F)
        while(b0.value == False):
            pass
        time.sleep(0.1)

    if(b1.value == False):
        print("b1 pressed")
        if(b1_view_changer == True):
            kbd.press(Keycode.V)
            kbd.release(Keycode.V)
            kbd.press(Keycode.ONE)
            kbd.release(Keycode.ONE)
            b1_view_changer = False
        
        elif(b1_view_changer == False):
            kbd.press(Keycode.V)
            kbd.release(Keycode.V)
            kbd.press(Keycode.THREE)
            kbd.release(Keycode.THREE)
            b1_view_changer = True
        while(b1.value == False):
            pass
        time.sleep(0.1)

    if(b2.value == False):
        print("b2 pressed")
        while(b2.value == False):
            pass
        time.sleep(0.1)

    if(b3.value == False):
        print("b3 pressed")
        kbd.press(Keycode.LEFT_ALT)
        kbd.press(Keycode.TAB)
        kbd.release(Keycode.TAB)
        ctr = 0
        first_loop = True
        while(True):
            if(b3.value == True and b6.value == True):
                ctr += 1
            time.sleep(0.01)
            if(ctr >= 50):
                break

            if(first_loop):
                r.value = False
                while(b3.value == False):
                    pass
                first_loop = False
                time.sleep(0.1)
                r.value = True

            if(b3.value == False):
                ctr = 0
                kbd.press(Keycode.RIGHT_ARROW)
                kbd.release(Keycode.RIGHT_ARROW)
                r.value = False
                time.sleep(0.1)
                r.value = True
            if(b6.value == False):
                ctr = 0
                kbd.press(Keycode.LEFT_ARROW)
                kbd.release(Keycode.LEFT_ARROW)
                b.value = False
                time.sleep(0.1)
                b.value = True

        kbd.release(Keycode.LEFT_ALT)
        time.sleep(0.1)

    if(b4.value == False):
        print("b4 pressed")
        while(b4.value == False):
            pass
        time.sleep(0.1)

    if(b5.value == False):
        print("b5 pressed")
        while(b5.value == False):
            pass
        time.sleep(0.1)

    if(b6.value == False):
        print("b6 pressed")
        while(b6.value == False):
            pass
        time.sleep(0.1)
       

    if(b7.value == False):
        print("b7 pressed")
        while(b7.value == False):
            pass
        time.sleep(0.1)