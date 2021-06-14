"""
FILE:       read_switches.py
AUTHOR:     Ben Simcox
PROJECT:    verbose-waffle (github.com/bnsmcx/verbose-waffle)
PURPOSE:    Currently simulates reading of switches.  This functionality will change when
            prototyping moves to hardware but the use of a list of lists to capture the
            switch positions will be the same.
"""


def read_switches() -> list:
    """This function will ultimately interact with the hardware, now it returns a test list"""
    test_list = [
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1]
    ]
    return test_list
