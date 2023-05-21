# Simple testfile! Change this file to test automation on GitHub

import main


def test_power():
    assert main.power(2, 2) == 4
    assert main.power(2, 3) == 6
