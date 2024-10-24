from typing import List, Optional

import pyray
from raylib import colors

from objects.base import BaseObject


class BaseScene:
    BACKGROUND_COLOR: pyray.Color = colors.BLACK

    def __init__(self, background_color: pyray.Color = None):
        if background_color:
            self.BACKGROUND_COLOR = background_color
        self.objects = self.get_objects()
        self.need_change_scene: bool = False
        self.additional_change_scene_info: Optional[int] = None

    def get_objects(self) -> List[BaseObject]:
        return []

    def set_scene(self, info: int) -> None:
        self.need_change_scene = True
        self.additional_change_scene_info = info

    def objects_call(self, method_name: str) -> None:
        for item in self.objects:
            method = getattr(item, method_name)
            method()

    def on_activate(self) -> None:
        self.objects_call('activate')
        self.additional_activate()

    def event(self) -> None:
        self.objects_call('event')
        self.additional_event()

    def logic(self) -> None:
        self.objects_call('logic')
        self.additional_logic()
        self.check_scene_change()

    def draw(self) -> None:
        pyray.clear_background(self.BACKGROUND_COLOR)
        self.objects_call('draw')
        self.additional_draw()

    def additional_activate(self) -> None:
        pass

    def additional_event(self) -> None:
        pass

    def additional_logic(self) -> None:
        pass

    def additional_draw(self) -> None:
        pass

    def check_scene_change(self) -> None:
        pass
