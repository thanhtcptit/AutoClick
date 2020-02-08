from pymouse import PyMouse


class Mouse(object):
    def __init__(self):
        self.m = PyMouse()

    def click(self, x, y):
        curr_pos = self.m.position()
        self.m.click(x, y, 1)
        self.m.move(curr_pos[0], curr_pos[1])