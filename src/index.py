"""Start the program and listeners"""

from typing import Type

from keyboard import on_press, unhook, wait

from .ui import Menu, UIBase


class State:
    """State class"""

    def __init__(self, start: Type[UIBase]) -> None:
        self.hook = None
        self.set(start)

    def set(self, new: Type[UIBase]) -> None:
        """Set the state"""
        self.ui = new()
        print(self.ui.render())

        if self.hook:
            unhook(self.hook)
        self.hook = on_press(self.ui.press)


def main() -> None:
    state = State(Menu)
    wait("esc")
