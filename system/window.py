import pyray

from system.settings import Settings


class Window:
    def __init__(self):
        settings = Settings()
        self.width = settings.WINDOW_WIDTH
        self.height = settings.WINDOW_HEIGHT
        self.title = settings.WINDOW_TITLE
        self.fps = settings.FPS
        self.exit_key = settings.EXIT_KEY
        self.is_initialised = False

    def init(self) -> None:
        self.is_initialised = True
        pyray.init_window(self.width, self.height, self.title)
        if self.fps:
            pyray.set_target_fps(self.fps)
        if self.exit_key:
            pyray.set_exit_key(self.exit_key)
