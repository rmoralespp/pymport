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
    expected = {
        "ignore": list(pymport.default_ignore_dirs),
        "files": list(),
        "quiet": False,
    }

    with unittest.mock.patch("pymport.do_help") as finish:
        result = pymport.do_get_arguments(arguments)
        assert result == expected
        finish.assert_called_once_with(header=header)


def test_do_help_help():
    arguments = ["--help"]
    expected = {
        "ignore": list(pymport.default_ignore_dirs),
        "files": list(),
        "quiet": False,
    }
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
    arguments = [str(filename)]
    expected = {
        "ignore": list(pymport.default_ignore_dirs),
        "files": [filename.expanduser()],
        "quiet": False,
    }
    with unittest.mock.patch("pymport.do_help") as finish:
        result = pymport.do_get_arguments(arguments)
        assert result == expected
        finish.assert_not_called()


def test_do_get_arguments_quiet():
    arguments = ["--quiet", "foo.py"]
    expected = {
        "files": [pathlib.Path("foo.py")],
        "ignore": list(pymport.default_ignore_dirs),
        "quiet": True,
    }
    result = pymport.do_get_arguments(arguments)
    assert result == expected


def test_do_get_arguments_ignore():
    arguments = ["--ignore=x", "--ignore=y", "foo.py"]
    expected = {
        "files": [pathlib.Path("foo.py")],
        "ignore": list(pymport.default_ignore_dirs) + ["x", "y"],
        "quiet": False,
    }
    result = pymport.do_get_arguments(arguments)
    assert result == expected
