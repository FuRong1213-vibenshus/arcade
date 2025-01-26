import random
import arcade
import os 
import enemy 
import laser 
import myShip
import emptyGameView
from settings import *


class GameView_1(emptyGameView.EmptyGameView):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = myShip.Ship(PATH_TO_MYSHIP, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the aliens
        for i in range(ALIEN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            alien = enemy.Alien(PATH_TO_ALIEN, SPRITE_SCALING_ALIEN)

            # Position the coin
            row_number = i//10
            col_number = i%10
            alien.center_x = col_number*(SCREEN_WIDTH/10) + 30
            alien.center_y = row_number*(SCREEN_HEIGHT/8) + 200

            # Add the coin to the lists
            self.alien_list.append(alien)

        # Set the background color
        arcade.set_background_color(arcade.color.BLUE)





