import pyray


class BaseObject:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.geometry = pyray.Rectangle(x, y, width, height)

    def activate(self) -> None:
        pass

    def event(self) -> None:
        pass

    def logic(self) -> None:
        pass

    def draw(self) -> None:
        pass

    def get_position(self) -> pyray.Vector2:
        return pyray.Vector2(self.geometry.x, self.geometry.y)

    def get_center(self) -> pyray.Vector2:
        return pyray.Vector2(self.geometry.x + self.geometry.width / 2, self.geometry.y + self.geometry.height / 2)

    def get_bottom_right(self) -> pyray.Vector2:
        return pyray.Vector2(self.geometry.x + self.geometry.width, self.geometry.y + self.geometry.height)
