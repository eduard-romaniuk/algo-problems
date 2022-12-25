import os
import time

import colored
from colored import stylize

from common import read_commands

DARK = '.'
LIT = '#'
POINTER = '_'
LIT_STYLE = colored.fg("red") + colored.attr("bold")
POINTER_STYLE = colored.fg("green") + colored.attr("bold")
CRT_WIDTH = 40
CRT_HEIGHT = 6
CRT_PIXEL_COUNT = CRT_WIDTH * CRT_HEIGHT

crt = [[DARK for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)]
cycle = 0
register = 1


def display(clear=True, stylized=True, delay=0.05, show_pointer=True):
    display_cycle = cycle + 1
    os.system('clear')
    print()
    print(f'CYCLE: {display_cycle}')
    print()
    for row, line in enumerate(crt):
        for col, cell in enumerate(line):
            if show_pointer:
                if row == cycle // CRT_WIDTH and col == cycle % CRT_WIDTH:
                    if stylized:
                        print(stylize(POINTER, POINTER_STYLE), end='')
                    else:
                        print(POINTER, end='')
                    continue
            if cell == DARK:
                if clear:
                    print(' ', end='')
                else:
                    print(DARK, end='')
                continue
            if cell == LIT:
                if stylized:
                    print(stylize(LIT, LIT_STYLE), end='')
                else:
                    print(LIT)
                continue
        print()
    time.sleep(delay)


for command in read_commands():
    row = cycle // CRT_WIDTH
    col = cycle % CRT_WIDTH

    if col in [register - 1, register, register + 1]:
        crt[row][col] = LIT

    if 'addx' in command:
        register += int(command.split(' ')[1])
    cycle += 1

    if cycle == CRT_PIXEL_COUNT:
        break

    display()
