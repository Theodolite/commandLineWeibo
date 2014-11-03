# -*- coding: utf-8 -*- 
import random
import curses


def init_color():
    """ initial color schemes for later use """
    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_BLUE, 0)
        curses.init_pair(2, curses.COLOR_CYAN, 0)
        curses.init_pair(3, curses.COLOR_GREEN, 0)
        curses.init_pair(4, curses.COLOR_MAGENTA, 0)
        curses.init_pair(5, curses.COLOR_RED, 0)
        curses.init_pair(6, curses.COLOR_YELLOW, 0)
        curses.init_pair(7, curses.COLOR_WHITE, 0)


class Curses(object):
    """ python curses library wrapper.
    The whole page includes a header, a content window and a command window.
    Header: display welcome;
    Content: main weibo text flow;
    Command window: where to write weibo and execuate other commands.
    """

    def __init__(self, scr=None):
        # init the curses setting
        # turn off echo; react to keys instantly; enable special keys
        self.stdscr = scr or curses.initscr()
        self.main_window = curses.newwin(60, 100, 3, 5)
        self.title_window = curses.newwin(3, 100, 0, 0)
        self.title_window.addstr("weili, comman line weibo from cizixs.")
        self.title_window.refresh()
        self.stdscr.keypad(1)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        init_color()

    def close(self):
        """ as opposed to initialization,
        restore everything back to normal
        """
        self.stdscr.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def get_key(self):
        """ return the key user pressed """
        return self.main_window.getch()

    def clear(self):
        """ clear the screen """
        self.main_window.clear()

    def puts(self, index, text, *cordinates):
        """ wrapper of addstr function which is easier to use. 
        write to screen with x,y mode instead of y,x mode.
        write to current postition by default.
        text: string to write
        cordinates: (x, y) tuple
        """
        self.main_window.attrset(curses.color_pair(index % 7 + 1))
        if not cordinates:
            self.main_window.addstr(text)
        else:
        	cor_x, cor_y = cordinates
        	self.main_window.addstr(cor_y, cor_x, text)
        self.main_window.attrset(0)
