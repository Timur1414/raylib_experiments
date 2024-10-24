from itertools import combinations
from typing import List

import pyray
from raylib import colors

from objects.base import BaseObject
from objects.images import Ball
from objects.texts import RecalculableText
from scenes.base import BaseScene
from system.settings import Settings


class GameScene(BaseScene):
    SCENE_SWITCH_TO_GAMEOVER: int = 0
    SCENE_SWITCH_TO_MENU: int = 1

    balls: List[Ball]
    collision_text: RecalculableText

    def __init__(self, background_color: pyray.Color = colors.BLACK):
        super().__init__(background_color)
        self.max_collision_count: int = 5
        self.collision_count = 0

    def get_objects(self) -> List[BaseObject]:
        self.collision_text = RecalculableText(
            x=10,
            y=10,
            text='Collisions: {collision_count}/{max_collision_count}',
            size=78,
            color=colors.WHITE
        )
        self.balls = [
            Ball(x=10, y=10, shift_x=1, shift_y=1),
            Ball(x=500, y=100, shift_x=-1, shift_y=1),
            Ball(x=400, y=500, shift_x=-1, shift_y=-1)
        ]
        return [
            *self.balls, self.collision_text]

    def additional_activate(self) -> None:
        self.collision_count = 0

    def additional_logic(self) -> None:
        self.collision_text.recreate_text(
            collision_count=self.collision_count,
            max_collision_count=self.max_collision_count
        )
        self.check_collisions()
        self.check_wall_collisions()

    @staticmethod
    def check_single_ball_wall_collision(ball: Ball) -> None:
        settings = Settings()
        if ball.get_position().x <= 0 or ball.get_bottom_right().x >= settings.WINDOW_WIDTH:
            ball.bounce(is_vertical=True)
        if ball.get_position().y <= 0 or ball.get_bottom_right().y >= settings.WINDOW_HEIGHT:
            ball.bounce(is_vertical=False)

    def check_wall_collisions(self) -> None:
        for item in self.balls:
            self.check_single_ball_wall_collision(ball=item)

    def check_scene_change(self) -> None:
        if pyray.is_key_down(pyray.KeyboardKey.KEY_ESCAPE):
            self.set_scene(info=self.SCENE_SWITCH_TO_MENU)
        if self.collision_count == self.max_collision_count:
            self.set_scene(info=self.SCENE_SWITCH_TO_GAMEOVER)

    def check_collision(self, first: Ball, second: Ball) -> None:
        if not first.collides_with(second):
            return
        first.collide(second)
        self.collision_count += 1

    def check_collisions(self) -> None:
        for pair in combinations(self.balls, 2):
            self.check_collision(first=pair[0], second=pair[1])

        # Это эквивалент следующего алгоритма (да ещё и работающий быстрее)
        # for i in range(len(self.balls) - 1):
        #     for j in range(i + 1, len(self.balls)):
        #         self.check_collision(self.balls[i], self.balls[j])
