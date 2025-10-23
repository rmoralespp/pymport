# -*- coding: utf-8 -*-

import pathlib
import unittest.mock

import pymport

header = (
    "Need at least one file or directory to check.",
    "",
)


def test_do_help_empty():
    arguments = list()
    expected = {"files": list()}
    with unittest.mock.patch("pymport.do_help") as finish:
        result = pymport.do_get_arguments(arguments)
        assert result == expected
        finish.assert_called_once_with(header=header)


def test_do_help_help():
    arguments = ["--help",]
    expected = {"files": list()}
    with unittest.mock.patch("pymport.do_help") as finish:
        result = pymport.do_get_arguments(arguments)
        assert result == expected
        finish.assert_has_calls(
            (
                unittest.mock.call(),
                unittest.mock.call(header=header),
            ),
        )


def test_do_help():
    # Test expanduser is called
    filename = pathlib.Path("~", "foo")
    arguments = [str(filename),]
    expected = {"files": [filename.expanduser()]}
    with unittest.mock.patch("pymport.do_help") as finish:
        result = pymport.do_get_arguments(arguments)
        assert result == expected
        finish.assert_not_called()
