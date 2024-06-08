import main_handler
import profile_freecad

#creating main handler
x = main_handler.MainHandler()

#creating a freecad handler object
x.add_profile(profile_freecad.FreecadProfile())

#starting the infinite loop
x.start_loop()
