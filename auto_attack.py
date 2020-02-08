from pymouse import PyMouse
import time
import sys


loop = 30
if len(sys.argv) > 1:
    loop = int(sys.argv[1])
print('Start in 3s')
m = PyMouse()
time.sleep(3)

for i in range(loop):
    print('{}/{}'.format(i + 1, loop), end='\r')
    m.click(902, 650)
    time.sleep(2.8)
    m.click(750, 620)
    time.sleep(2.2)
