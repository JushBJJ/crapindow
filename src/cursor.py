"""
Cursor class that will be responible for the terminal cursor.
"""

import colorama


class Cursor:
    """
            Cursor class is just to make my life easier by positioning the
            cursor within menus and other stuff needed.

            It automatically defaults the x and y for certain reasons
            that break the command prompt.

            It has input function that finds simply returns the arrow or
            wasd keys that will be used to position the cursor.

            pos is used to position the cursor.
    """

    def __init__(self, scr):
        """ Automatically sets the cursor position to x:1, y:1 """

        self.screen = scr
        self.x, self.y = 1, 1

        self.last_screen_dimensions = {
            "width": int(self.screen.get_width()),
            "height": int(self.screen.get_height())
        }
        self.saved_positions = {}

    def correct_position(self):
        """ Corrects the position of self.x and self.y
            Only Applies if the screen width or height
            gets smaller """

        width = self.screen.get_width()
        height = self.screen.get_height()

        if self.last_screen_dimensions["width"] > width:
            self.x -= self.last_screen_dimensions["width"] - width

        if self.last_screen_dimensions["height"] > height:
            self.y -= self.last_screen_dimensions["height"] - height

    def save_position(self, name, position):
        """ Saves the positions, used for menu selection
            Position type must be a list containing [x,y] """

        self.saved_positions[name] = {}
        self.saved_positions[name]["x"] = position[0]
        self.saved_positions[name]["y"] = position[1]

    def delete_position(self, name):
        if name in self.saved_positions:
            del self.saved_positions[name]

    def load_position(self, name):
        """ Moves the cursor to the cursor position """

        x = self.saved_positions[name]["x"]
        y = self.saved_positions[name]["y"]

        self.pos(x, y)

    def pos(self, x, y):
        """ Moves the cursor to the given position. """

        if isinstance(x, float):
            x = int(x)

        self.screen.write(colorama.Cursor.POS(x, y), ansi=True)
        self.x = x
        self.y = y

        return x, y

    def reset_pos(self):
        """ Resets the cursor position to 1,1 """

        return self.pos(1, 1)

    def pos_up(self, y=1):
        """ Moves the cursor up by y """

        self.y -= y
        return self.pos(self.x, self.y)

    def pos_down(self, y=1):
        """ Moves the cursor down by y """

        self.y += y
        return self.pos(self.x, self.y)

    def pos_left(self, x=1):
        """ Moves the cursor left by x """

        self.x -= x
        return self.pos(self.x, self.y)

    def pos_right(self, x=1):
        """ Moves the cursor right by x """

        self.x += x
        return self.pos(self.x, self.y)
