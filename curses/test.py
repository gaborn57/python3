#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-
import time
import curses

stdscr = curses.initscr()

#curses.curs_set(0)              # enlève le curseur
#curses.noecho()                 # évite un echo en tapant une touche
#curses.cbreak()                 # demap touche 'a' vers caractère 'a', etc
#stdscr.keypad(True)             # demap le keypad

def wrap(stdscr):
  stdscr.addstr(2,4,"Hello Alex")
  stdscr.refresh()
  time.sleep(2)

curses.wrapper(wrap)

#curses.echo()                   # remet tout comme avant
#curses.nocbreak()               # idem
#stdscr.keypad(False)            # idem
#curses.endwin()
