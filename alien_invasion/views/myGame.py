import arcade
import os
import instructionView
from settings import *


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Alien Invasion!")
    start_view = instructionView.InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
