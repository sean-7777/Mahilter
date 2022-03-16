from keyboard import KeyboardEvent


class UIBase:
    def render(self) -> str:
        return ""

    def press(self, key: KeyboardEvent) -> None:
        pass
