import pyray


class Settings:
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    WINDOW_TITLE: str = 'Hello, raylib'
    FPS: int = 120
    EXIT_KEY: pyray.KeyboardKey = pyray.KeyboardKey.KEY_F8
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
