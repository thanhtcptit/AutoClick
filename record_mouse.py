from threading import Thread
from EventListener import *
import time

mouse_listener = MouseListener()
keyboard_listener = KeyboardListener(mouse_listener)


def run_listener(rtype):
    if rtype == 1:
        print('Mouse listener is running')
        mouse_listener.run()
    else:
        print('Keyboard listener is running')
        keyboard_listener.run()


t1 = Thread(target=run_listener, args=(1,))
t2 = Thread(target=run_listener, args=(2,))
t1.start()
t2.start()
print('Join thread')
t1.join()
t2.join()
print('Finish')