from __future__ import annotations

import os

import pyray
from raylib import colors

from objects.base import BaseObject


class Image(BaseObject):
    filename = None

    def __init__(self, x: int, y: int):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f'Изображение {self.filename} не найдено')
        image = pyray.load_image(self.filename)
        self.texture = pyray.load_texture_from_image(image)
        pyray.unload_image(image)
        super().__init__(x, y, self.texture.width, self.texture.width)

    def __del__(self):
        if not hasattr(self, 'texture'):
            return
        pyray.unload_texture(self.texture)

    def draw(self) -> None:
        pyray.draw_texture_v(self.texture, self.get_position(), colors.WHITE)


class Ball(Image):
    filename = 'images/basketball.png'

    def __init__(self, x: int, y: int, shift_x: int, shift_y: int):
        super().__init__(x, y)
        self.initial = {
            'x': x,
            'y': y,
            'shift_x': shift_x,
            'shift_y': shift_y
        }
        self.shift = pyray.Vector2(shift_x, shift_y)

    def activate(self) -> None:
        self.geometry.x = self.initial['x']
        self.geometry.y = self.initial['y']
        self.shift.x = self.initial['shift_x']
        self.shift.y = self.initial['shift_y']

    def logic(self) -> None:
        self.geometry.x += self.shift.x
        self.geometry.y += self.shift.y

    def get_radius(self) -> float:
        return self.geometry.width / 2

    def collides_with(self, other: Ball) -> bool:
        return pyray.check_collision_circles(
            self.get_center(),
            self.get_radius(),
            other.get_center(),
            other.get_radius()
        )

    def collide(self, other: Ball) -> None:
        self.shift, other.shift = other.shift, self.shift

    def bounce(self, is_vertical: bool):
        if is_vertical:
            self.shift.x *= -1
        else:
            self.shift.y *= -1
