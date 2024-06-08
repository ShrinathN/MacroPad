from main_handler import BaseProfile

class FreecadProfile(BaseProfile):

    def __init__(self):
        print("Freecad profile object created")
        super().__init__()

    def loop_handler(self, main_handler_object_ptr):
        #looping over all the buttons and stuff

        if(main_handler_object_ptr.__get_button_status()[0]):
            print("Button 1 pressed")
            main_handler_object_ptr.set_rgb(True, False, False)
            while(main_handler_object_ptr.__get_button_status()[0]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[1]):
            print("Button 2 pressed")
            main_handler_object_ptr.set_rgb(False, True, False)
            while(main_handler_object_ptr.__get_button_status()[1]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[2]):
            print("Button 3 pressed")
            main_handler_object_ptr.set_rgb(False, False, True)
            while(main_handler_object_ptr.__get_button_status()[2]):
                main_handler_object_ptr.keyboard_register(97)
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[3]):
            print("Button 4 pressed")
            main_handler_object_ptr.set_rgb(True, True, False)
            while(main_handler_object_ptr.__get_button_status()[3]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[4]):
            print("Button 5 pressed")
            main_handler_object_ptr.set_rgb(True, False, True)
            while(main_handler_object_ptr.__get_button_status()[4]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[5]):
            print("Button 6 pressed")
            main_handler_object_ptr.set_rgb(False, True, True)
            while(main_handler_object_ptr.__get_button_status()[5]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[6]):
            print("Button 7 pressed")
            main_handler_object_ptr.set_rgb(True, True, True)
            while(main_handler_object_ptr.__get_button_status()[6]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[7]):
            print("Button 8 pressed")
            main_handler_object_ptr.set_rgb(False, False, False)
            while(main_handler_object_ptr.__get_button_status()[7]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[8]):
            print("Button 9 pressed")
            main_handler_object_ptr.set_rgb(False, False, False)
            while(main_handler_object_ptr.__get_button_status()[8]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[9]):
            print("Button 10 pressed")
            main_handler_object_ptr.set_rgb(False, False, False)
            while(main_handler_object_ptr.__get_button_status()[9]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)


        if(main_handler_object_ptr.__get_button_status()[10]):
            print("Button 11 pressed")
            main_handler_object_ptr.set_rgb(False, False, False)
            while(main_handler_object_ptr.__get_button_status()[10]):
                pass
            main_handler_object_ptr.set_rgb(False, False, False)

        #if no normal button is pressed
        if(not main_handler_object_ptr.__no_normal_button_is_pressed()):
            main_handler_object_ptr.set_rgb(False, False, False)

        return super().loop_handler(main_handler_object_ptr)