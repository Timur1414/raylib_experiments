from typing import List

import pyray
from raylib import colors

from objects.base import BaseObject
from objects.button import Button
from objects.lines import AnimatedLine
from scenes.base import BaseScene
from system.settings import Settings


class MenuScene(BaseScene):
    SCENE_SWITCH_TO_GAME: int = 0
    BACKGROUND_COLOR: pyray.Color = colors.BLACK
    buttons: List[Button]
    lines: List[AnimatedLine]

    def get_objects(self) -> List[BaseObject]:
        self.buttons = self.get_buttons()
        self.lines = self.get_lines()
        return [*self.buttons, *self.lines]

    @staticmethod
    def get_lines():
        return [
            AnimatedLine(
                start_position=pyray.Vector2(100, 100),
                finish_position=pyray.Vector2(700, 100),
                color=colors.WHITE,
                thickness=4,
                seconds_to_animate=3
            ),
            AnimatedLine(
                start_position=pyray.Vector2(700, 100),
                finish_position=pyray.Vector2(700, 500),
                color=colors.WHITE,
                thickness=4,
                seconds_to_animate=3
            ),
            AnimatedLine(
                start_position=pyray.Vector2(700, 500),
                finish_position=pyray.Vector2(100, 500),
                color=colors.WHITE,
                thickness=4,
                seconds_to_animate=3
            ),
            AnimatedLine(
                start_position=pyray.Vector2(100, 500),
                finish_position=pyray.Vector2(100, 100),
                color=colors.WHITE,
                thickness=4,
                seconds_to_animate=3
            )
        ]

    def get_buttons(self):
        settings = Settings()
        return [
            Button(
                x=settings.WINDOW_WIDTH // 2 - 100 // 2,
                y=settings.WINDOW_HEIGHT // 2 - 10 - 50,
                width=100,
                height=50,
                title='New game',
                action=self.new_game_button_action
            ),
            Button(
                x=settings.WINDOW_WIDTH // 2 - 100 // 2,
                y=settings.WINDOW_HEIGHT // 2 + 10,
                width=100,
                height=50,
                title='Exit',
                action=self.exit_button_action
            )
        ]

    def new_game_button_action(self) -> None:
        self.set_scene(self.SCENE_SWITCH_TO_GAME)

    @staticmethod
    def exit_button_action() -> None:
        pyray.close_window()
        exit(0)
