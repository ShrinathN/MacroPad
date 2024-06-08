import random
import time
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode
from lib.adafruit_hid.consumer_control import ConsumerControl
from lib.adafruit_hid.consumer_control_code import ConsumerControlCode
import digitalio
import board
import usb_hid


class MainHandler:

    def __init__(self):
        # keyboard
        self.kbd = Keyboard(usb_hid.devices)
        # consumer = ConsumerControl(usb_hid.devices)
        # consumer.send(ConsumerControlCode.PLAY_PAUSE)
        self.b1 = digitalio.DigitalInOut(board.GP0)
        self.b1.direction = digitalio.Direction.INPUT
        self.b2 = digitalio.DigitalInOut(board.GP1)
        self.b2.direction = digitalio.Direction.INPUT
        self.b3 = digitalio.DigitalInOut(board.GP2)
        self.b3.direction = digitalio.Direction.INPUT
        self.b4 = digitalio.DigitalInOut(board.GP3)
        self.b4.direction = digitalio.Direction.INPUT
        self.b5 = digitalio.DigitalInOut(board.GP4)
        self.b5.direction = digitalio.Direction.INPUT
        self.b6 = digitalio.DigitalInOut(board.GP5)
        self.b6.direction = digitalio.Direction.INPUT
        self.b7 = digitalio.DigitalInOut(board.GP6)
        self.b7.direction = digitalio.Direction.INPUT
        self.b8 = digitalio.DigitalInOut(board.GP7)
        self.b8.direction = digitalio.Direction.INPUT
        self.b9 = digitalio.DigitalInOut(board.GP8)
        self.b9.direction = digitalio.Direction.INPUT
        self.b10 = digitalio.DigitalInOut(board.GP9)
        self.b10.direction = digitalio.Direction.INPUT
        self.b11 = digitalio.DigitalInOut(board.GP10)
        self.b11.direction = digitalio.Direction.INPUT
        self.b12 = digitalio.DigitalInOut(board.GP11)
        self.b12.direction = digitalio.Direction.INPUT

        # initialising LED
        self.r = digitalio.DigitalInOut(board.GP14)
        self.r.direction = digitalio.Direction.OUTPUT
        self.r.value = True
        self.g = digitalio.DigitalInOut(board.GP13)
        self.g.direction = digitalio.Direction.OUTPUT
        self.g.value = True
        self.b = digitalio.DigitalInOut(board.GP12)
        self.b.direction = digitalio.Direction.OUTPUT
        self.b.value = True

        # initialising profile stuff
        self.profile_list = []
        self.profile_count = 0
        self.current_profile = 0

    def keyboard_register(self, keycode):
        self.kbd.press(keycode)
        self.kbd.release(keycode)

    def set_rgb(self, red, green, blue):
        if (red):
            self.r.value = False
        else:
            self.r.value = True
        if (green):
            self.g.value = False
        else:
            self.g.value = True
        if (blue):
            self.b.value = False
        else:
            self.b.value = True

    def __set_current_profile(self, prof):
        print(f"Switching to profile {str(prof)}")
        self.current_profile = prof

    def __profile_switch_pressed(self):
        return self.__get_button_status()[11]

    def __no_normal_button_is_pressed(self):
        return ((not self.__get_button_status()[0]) and (not self.__get_button_status()[1]) and (not self.__get_button_status()[2]) and (not self.__get_button_status()[3]) and (not self.__get_button_status()[4]) and (not self.__get_button_status()[5]) and (not self.__get_button_status()[6]) and (not self.__get_button_status()[7]) and (not self.__get_button_status()[8]) and (not self.__get_button_status()[9]) and (not self.__get_button_status()[10]))
    
    def __run_current_loop_handler(self):
        self.profile_list[self.current_profile].loop_handler(self)

    def __profile_switch_sequence(self):
        if (self.__profile_switch_pressed()):  # if button 12 is pressed
            print("Profile switch button pressed")
            # flash red while the button12 is pressed and none of the other buttons are pressed
            while (self.__profile_switch_pressed() and self.__no_normal_button_is_pressed()):
                # flashing red
                self.set_rgb(True, False, False)
                time.sleep(50e-3)  # sleep for 50ms
                self.set_rgb(False, False, False)
                time.sleep(50e-3)  # sleep for 50ms
            time.sleep(500e-3) #sleeping for 500ms

            #changing profile
            self.__profile_change()

    def __profile_change(self):
        buttons_status = self.__get_button_status()
        for i in range(0, len(buttons_status) - 1):
            if(buttons_status[i]):
                if(i <= (len(self.profile_list) - 1)):
                    self.__set_current_profile(i)
                    break

    def start_loop(self):
        print("Main loop started")

        while (True):

            #running current profile loop handler
            self.__run_current_loop_handler()

            # switching profile
            self.__profile_switch_sequence()

            time.sleep(10e-3)  # sleep for 10ms every loop

    def __get_button_status(self):
        to_return = [not self.b1.value, not self.b2.value, not self.b3.value, not self.b4.value, not self.b5.value, not self.b6.value,
                     not self.b7.value, not self.b8.value, not self.b9.value, not self.b10.value, not self.b11.value, not self.b12.value]
        return to_return

    def add_profile(self, profile_object):
        self.profile_list.append(profile_object)


class BaseProfile:

    def __init__(self) -> None:
        pass

    def loop_handler(self, main_handler_object_ptr):
        pass
