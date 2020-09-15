import arcade

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200
WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10
BLOCK_X = 10
BLOCK_Y = 10

class MyGame(arcade.Window):
    """
    Main application class
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        render the screen
        """


        arcade.start_render()
        for i in range(ROW_COUNT):
            for i in range(COLUMN_COUNT):
                arcade.draw_rectangle_filled(BLOCK_X,BLOCK_Y,WIDTH-MARGIN*2,HEIGHT-MARGIN*2,arcade.color.WHITE,)
                BLOCK_X += 20
            BLOCK_Y += 20

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button
        """
        pass

def main():

    window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()
if __name__ == "__main__":
    main()