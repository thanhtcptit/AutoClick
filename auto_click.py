from pymouse import PyMouse
from datetime import datetime
import time
import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('trigger_time', type=str)
    parser.add_argument('click_attempt', type=int, default=1)

    return parser.parse_args()


args = _parse_args()
time.sleep(3)
m = PyMouse()
x = (199, 287)
now = datetime.now()
hour = int(args.trigger_time[:2])
minute = int(args.trigger_time[:3:])
trigger_time = now.replace(hour=hour, minute=minute)
click_attempt = args.click_attempt

while True:
    now = datetime.now()
    if now >= trigger_time:
        m.click(x[0], x[1])
        click_attempt -= 1
        if click_attempt == 0:
            break
    time.sleep(5)
