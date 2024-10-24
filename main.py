import pyray

from system.application import Application
from system.window import Window


def main():
    window = Window()
    window.init()
    application = Application(window=window)
    application.main_loop()
    pyray.close_window()
    exit(0)


if __name__ == '__main__':
    main()
