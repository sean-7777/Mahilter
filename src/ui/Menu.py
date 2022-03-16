from .UIBase import UIBase


class Menu(UIBase):
    def render(self):
        return """
            1. Exit
        """

    def press(self, evt):
        if evt.name == "1":
            print(5)
        else:
            print(evt.name)
