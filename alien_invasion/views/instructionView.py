import arcade
from settings import *
import gameView_child1

class InstructionView(arcade.View):
    """ View to show instructions"""
    def on_show_view(self):
        """ This is run once when we switch to this view"""
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        # TODO: Add more intructions here if needed
        arcade.draw_text("Instructions Screen", self.window.width/2, self.window.height/2, arcade.color.WHITE, font_size=50, anchor_x = "center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = gameView_child1.GameView_1()
        game_view.setup()
        self.window.show_view(game_view)


