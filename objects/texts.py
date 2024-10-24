import pyray

from objects.base import BaseObject


class Text(BaseObject):
    def __init__(self, x: int, y: int, text: str, size: int, color: pyray.Color, width=0, height=0):
        super().__init__(x, y, width, height)
        self.text = text
        self.size = size
        self.color = color

    def draw(self) -> None:
        pyray.draw_text(self.text, int(self.geometry.x), int(self.geometry.y), self.size, self.color)


class RecalculableText(Text):
    def __init__(self, x: int, y: int, text: str, size: int, color: pyray.Color):
        super().__init__(x, y, text, size, color)
        self.text_format = text

    def recreate_text(self, **kwargs) -> None:
        self.text = self.text_format.format(**kwargs)
