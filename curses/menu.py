#! /usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 2 -*-

import curses
import time


menu = ('Home','Play','Scoreboard','Quit')

def print_menu(stdscr, indice):
  stdscr.clear()
  h,w = stdscr.getmaxyx()
  for idx, i in enumerate(menu):
    x = (w-len(i))//2
    y = (h-len(menu))//2+idx
    if idx == indice:
      stdscr.attron(curses.color_pair(1))
      stdscr.addstr(y, x, i)
      stdscr.attroff(curses.color_pair(1))
    else:
      stdscr.addstr(y, x, i)
  stdscr.refresh()
  

def wrap(stdscr):
  curses.curs_set(0)
  indice = 0
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  print_menu(stdscr, indice)

  while 1:
    stdscr.clear()
    if key == curses.KEY_UP and indice > 0:
      indice-=1
    elif key == curses.KEY_DOWN and indice < len(menu)-1:
      indice+=1
    elif key == curses.KEY_ENTER or key in [10,13]:
      stdscr.addstr(0,0, 'You just pressed {}'.format(menu[indice]))
      stdscr.refresh()
      stdscr.getch()
      if menu[indice] == 'Quit':
        break
    print_menu(stdscr, indice)
  
curses.wrapper(wrap)
