import datetime

import pyray

from objects.base import BaseObject


class AnimatedLine(BaseObject):
    def __init__(self, start_position: pyray.Vector2, finish_position: pyray.Vector2,
                 color: pyray.Color, thickness: int, seconds_to_animate: int):
        super().__init__(
            start_position.x, start_position.y,
            finish_position.x - start_position.x,  # can be negative due to animation issues
            finish_position.y - start_position.y,
        )
        self.start_position = start_position
        self.finish_position = finish_position
        self.color = color
        self.thickness = thickness
        self.seconds_to_animate = seconds_to_animate
        self.motion_start = datetime.datetime.now()
        self.motion_now = datetime.datetime.now()
        self.percent_completed = 0

    def activate(self) -> None:
        self.motion_start = datetime.datetime.now()
        self.percent_completed = 0

    def logic(self) -> None:
        self.motion_now = datetime.datetime.now()
        delta = (self.motion_now - self.motion_start)
        ms = delta.seconds * 1000000 + delta.microseconds
        self.percent_completed = min(1.0, ms / (self.seconds_to_animate * 1000000))

    def get_current_finish_position(self) -> pyray.Vector2:
        return pyray.Vector2(
            self.start_position.x + self.geometry.width * self.percent_completed,
            self.start_position.y + self.geometry.height * self.percent_completed,
        )

    def draw(self) -> None:
        pyray.draw_line_ex(
            self.start_position,
            self.get_current_finish_position(),
            self.thickness,
            self.color
        )
