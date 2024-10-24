from typing import Callable

import pyray

from objects.base import BaseObject


class Button(BaseObject):

    def default_action(self):
        pass

    def __init__(self, x: int, y: int, width: int, height: int, title: str, action: Callable = None):
        super().__init__(x, y, width, height)
        self.title = title
        self.action: Callable = action if action else self.default_action

    def event(self) -> None:
        if not pyray.gui_button(self.geometry, self.title):
            return
        self.action()
