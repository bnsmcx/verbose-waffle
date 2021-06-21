"""
FILE:       main.py
AUTHOR:     Ben Simcox
PROJECT:    verbose-waffle (github.com/bnsmcx/verbose-waffle)
PURPOSE:    This file is the main entry point for the app.
"""
import time

from read_switches import read_switches
from write_to_display import write_to_display


def byte_to_char(byte: str) -> str:
    """translate a binary byte into an ASCII Character"""
    return chr(int(byte, base=2))


def process_switch_positions(switch_positions: list) -> list:
    """iterate through the list of binary switch positions, return the ascii equivalent"""
    ascii_characters = []
    for byte in switch_positions:
        byte_as_string = ""
        for switch in byte:
            byte_as_string += str(switch)
        character = byte_to_char(byte_as_string)
        ascii_characters.append(character)
    return ascii_characters


def main():
    """main function"""
    while True:
        switch_positions = read_switches()
        text = process_switch_positions(switch_positions)
        write_to_display(text)
        time.sleep(3)


if __name__ == '__main__':
    main()
