from typing import List, Dict

import pyray

from scenes.base import BaseScene
from scenes.game import GameScene
from scenes.gameover import GameOverScene
from scenes.menu import MenuScene
from system.window import Window

RoutingList = List[Dict[int, int]]


class Application:
    MENU_SCENE_INDEX: int = 0
    GAME_SCENE_INDEX: int = 1
    GAMEOVER_SCENE_INDEX: int = 2

    SCENES_ROUTING: RoutingList = [
        {0: GAME_SCENE_INDEX},
        {0: GAMEOVER_SCENE_INDEX, 1: MENU_SCENE_INDEX},
        {0: MENU_SCENE_INDEX, 1: MENU_SCENE_INDEX}
    ]

    def __init__(self, window: Window):
        if not isinstance(window, Window):
            raise ValueError('Некорректный тип объекта окна')
        if not window.is_initialised:
            raise RuntimeError('Для работы приложения окно должно быть инициализировано. Запустите window.init()')
        self.window = window
        self.current_scene_index: int = 0
        self.scenes: List[BaseScene] = [
            MenuScene(),
            GameScene(),
            GameOverScene()
        ]

    @property
    def current_scene(self) -> BaseScene:
        return self.scenes[self.current_scene_index]

    def draw(self) -> None:
        pyray.begin_drawing()
        self.current_scene.draw()
        self.additional_draw()
        pyray.end_drawing()

    def check_scene_change(self) -> None:
        if not self.current_scene.need_change_scene:
            return
        info = self.current_scene.additional_change_scene_info
        target_scene_index = self.SCENES_ROUTING[self.current_scene_index][info]
        self.current_scene.need_change_scene = False
        self.current_scene_index = target_scene_index
        self.current_scene.on_activate()

    def main_loop(self) -> None:
        while not pyray.window_should_close():
            self.check_scene_change()
            self.current_scene.event()
            self.current_scene.logic()
            self.draw()

    def additional_draw(self) -> None:
        pass
