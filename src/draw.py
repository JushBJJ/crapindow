"""
Draw functions

Supported shapes:
    - Rectangle
"""

from screen import foreground_colours, background_colours
# Rectangles in this case are automatically unfilled.


class Rectangle:
    """ Rectangle class for drawing boxes for the photocopier """

    def __init__(self, scr, width, height, x, y, **kwargs):
        self.screen = scr

        # Dimensions
        self.width = width
        self.height = height

        # Position
        self.x = x
        self.y = y

        # Rectangle Configurations
        self.foreground = kwargs["foreground"]
        self.background = kwargs["background"]
        self.filled = kwargs["filled"]
        self.char = kwargs["char"]

    def draw(self, x, y):
        """ Draw function using whatever key is specifed """

        # Draw rectangle.
        for line in range(y, y+self.height+1):
            self.screen.cursor.to_pos(x, line)

            if line in (y, y+self.height):
                self.screen.pre_write(self.char*(self.width+1))

            else:
                self.screen.pre_write(self.char)
                self.screen.cursor.to_pos(x+self.width, line)
                self.screen.pre_write(self.char)

        self.screen.flush()

    def write(self, x, y, string):
        """ Write function to put strings into boxes.

            Dimensions of a rectange (example)
              01234567
            0 --------
            1 -      -
            2 -      -
            3 --------
        """

        x += self.x
        y += self.y

        self.screen.cursor.to_pos(x, y)

        # Write string in position
        for letter in string:
            if x == self.x+self.width:
                break

            self.screen.write(letter, flush=False)
            x += 1

        self.screen.flush()

    def to_pos(self, x, y):
        """ Move cursor relative to the box dimensions """

        self.screen.cursor.to_pos(x+self.x, y+self.y)
