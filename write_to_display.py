"""
FILE:       write_to_display.py
AUTHOR:     Ben Simcox
PROJECT:    verbose-waffle (github.com/bnsmcx/verbose-waffle)
PURPOSE:    Currently this simulates writing to the displays by simply printing a list
            of characters.  Once prototyping moves to hardware that logic will be implemented
            but the use of a list of characters will persist.
"""


def write_to_display(text: list):
    """Eventually this will interact with the hardware displays, now it just prints the text"""
    print(str(text))
