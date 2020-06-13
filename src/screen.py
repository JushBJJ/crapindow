""" Basically the whole terminal screen itself. """


import sys
import os
import colorama
import cursor


class Screen:
    """
            Screen class basically initialises the screen which will modify
            stdout.

            Includes clear_line, clear_screen, manual flushing and getting the
            screen amount of columns and lines
    """

    def __init__(self):
        """ Automatically initialises the terminal and cursor. """

        colorama.init(wrap=True)  # Wraps stdout to enable most ansi support
        self.stdout = sys.stdout
        self.cursor = cursor.Cursor(self)
        self.cursor.pos(self.get_width()-1, self.get_height()-1)

        self.width = self.get_width()
        self.height = self.get_height()

        self.clear_screen()

        # foreground_colours and background_colours is pretty much copy and-
        # pasted from colourama's ansi source
        # but put into a dictionary just so things are easier when printing
        # out forground colours

        self.foreground_colours = {
            "BLACK": "\x1b[30m",
            "RED": "\x1b[31m",
            "GREEN": "\x1b[32m",
            "YELLOW": "\x1b[33m",
            "BLUE": "\x1b[34m",
            "MAGENTA": "\x1b[35m",
            "CYAN": "\x1b[36m",
            "WHITE": "\x1b[37m",
            "RESET": "\x1b[39m"
        }

        self.background_colours = {
            "BLACK": "\x1b[40m",
            "RED": "\x1b[41m",
            "GREEN": "\x1b[42m",
            "YELLOW": "\x1b[43m",
            "BLUE": "\x1b[44m",
            "MAGENTA": "\x1b[45m",
            "CYAN": "\x1b[46m",
            "WHITE": "\x1b[47m",
            "RESET": "\x1b[49m"
        }

    def foreground_colour(self, colour, flush=True):
        """ Change foreground colour (text colour) """

        self.write(self.foreground_colours[colour], flush=flush)

    def background_colour(self, colour, flush=True):
        """ Change background colour """

        self.write(self.background_colours[colour], flush=flush)

    def flush(self):
        """ Flushes stdout """

        self.stdout.flush()

    def autoposition(self, string):
        """ This automatcally updates the position variables of the cursor.
            Can possibly lead to peformance issues within writing to stdout """

        for char in string:
            if char == "\n":
                self.cursor.x = 1
                self.cursor.y += 1
            else:
                self.cursor.x += len(char)

    def write(self, string, ansi=False, flush=True):
        """ Manually writes stdout and automatically updates cursor position
            If ansi is true, it doesn't update the cursor position. """

        self.stdout.write(string)

        if flush:
            self.stdout.flush()

        if not ansi:
            self.autoposition(string)

    def clear_line(self):
        """ Clears the current line the cursor is in. """

        self.write(colorama.ansi.clear_line(), ansi=True)

    def clear_screen(self):
        """ Clears the screen by moving the cursor to the end of the
            terminal screen and calls ansi sequence.
            Puts the cursor at the end of the terminal screen """

        self.cursor.pos(self.get_width(), self.get_height())
        self.write(colorama.ansi.clear_screen())
        self.cursor.reset_pos()

    def get_width(self):
        """ Get the amount of columns of the terminal
        (constantly updated automatically) """

        return os.get_terminal_size()[0]-1

    def get_height(self):
        """ Get the amount of lines of th terminal
        (constantly updated automatically) """

        return os.get_terminal_size()[1]-1
