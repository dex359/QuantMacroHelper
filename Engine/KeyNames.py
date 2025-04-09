from pynput import keyboard


class KeyboardHandler:

    def __init__(self, container, refresh):
        self.container = {}
        self.refresh = refresh
        self.listener = keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release
        )

    def on_press(self, key):
        if not key in self.container:
            self.container[key] = "hhh"
#            self.refresh()

    def on_release(self, key):
        print(key in self.container)
        #self.container.remove(key)
#        self.refresh()

class Tester:

    def __init__(self):
        self.container = []
        self.handler = KeyboardHandler(
            self.container,
            self.refresh
        )

    def refresh(self):
        print(" " * 120, end = "\r", flush = True)
        print(", ".join(str(key) for key in self.container), end = "\r", flush = True)

    def start(self):
        print("Keyboard tester. List of pressed keys:")
        self.handler.listener.start()
        self.handler.listener.join()

if __name__ == "__main__":
    test = Tester()
    test.start()