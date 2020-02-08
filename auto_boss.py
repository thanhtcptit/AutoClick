from MouseInterface import Mouse
import time

x1 = (684, 527)
x2 = (1009, 740)
x3 = (727, 580)
#x3 = (728, 619)

time.sleep(2)
m = Mouse()
while True:
    m.click(x1[0], x1[1])
    time.sleep(2)
    m.click(x2[0], x2[1])
    time.sleep(2.5)
    m.click(x3[0], x3[1])
    time.sleep(25.5)

