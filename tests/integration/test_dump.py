# -*- coding: utf-8 -*-

import unittest.mock

import pymport


def test_dump_results_1():
    items = (
        (
            (1, 2, 3),
            (4, 5, 6),
        ),
    )
    with unittest.mock.patch("pymport.print") as printer:
        result = pymport.dump_results(items)
        assert result == 1
        printer.assert_has_calls(
            (
                unittest.mock.call("1:2: 3"),
                unittest.mock.call("4:5: 6"),
            ),
        )


def test_dump_results_0():
    items = ()
    with unittest.mock.patch.object(pymport, "print") as printer:
        result = pymport.dump_results(items)
        assert result == 0
        printer.assert_not_called()
