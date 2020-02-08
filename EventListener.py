from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent


class MouseListener(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.mouse_clicks = []

    def click(self, x, y, button, press):
        if press is False:
            return
        self.mouse_clicks.append([x, y, button, press])
        print('({}, {}) {}'.format(x, y, button))


class KeyboardListener(PyKeyboardEvent):
    def __init__(self, m_listener):
        PyKeyboardEvent.__init__(self)
        self.mouse_listener = m_listener

    def tap(self, keycode, character, press):
        if press is False:
            return
        print('{} {}'.format(keycode, character))
        if character == 'q':
            try:
                self.mouse_listener.stop()
            except Exception:
                print('Stop listener')
                exit(0)

