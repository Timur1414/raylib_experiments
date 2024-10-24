import datetime
from typing import List

import pyray
from raylib import colors

from objects.base import BaseObject
from objects.texts import RecalculableText
from scenes.base import BaseScene


class GameOverScene(BaseScene):
    SCENE_SWITCH_TO_MENU_BY_TIME: int = 0
    SCENE_SWITCH_TO_MENU_BY_ESC: int = 1
    gameover_text: RecalculableText

    def __init__(self, background_color: pyray.Color = colors.BLACK):
        super().__init__(background_color)
        self.max_wait_seconds = 3
        self.wait_seconds = 0
        self.open_scene_datetime = datetime.datetime.now()

    def get_objects(self) -> List[BaseObject]:
        self.gameover_text = RecalculableText(
            x=100,
            y=250,
            text='Game over ({seconds}/{seconds_max})',
            size=78,
            color=colors.RED
        )
        return [self.gameover_text]

    def additional_activate(self) -> None:
        self.open_scene_datetime = datetime.datetime.now()

    def check_scene_change(self) -> None:
        if pyray.is_key_down(pyray.KeyboardKey.KEY_ESCAPE):
            self.set_scene(self.SCENE_SWITCH_TO_MENU_BY_ESC)
        if self.wait_seconds >= self.max_wait_seconds:
            self.set_scene(self.SCENE_SWITCH_TO_MENU_BY_TIME)

    def additional_logic(self) -> None:
        now = datetime.datetime.now()
        self.wait_seconds = (now - self.open_scene_datetime).seconds
        self.gameover_text.recreate_text(seconds=self.wait_seconds, seconds_max=self.max_wait_seconds)
