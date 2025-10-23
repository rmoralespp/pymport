# -*- coding: utf-8 -*-

import unittest.mock

import pymport


def test_do_help():
    with (
        unittest.mock.patch("pymport.sys.exit") as finish,
        unittest.mock.patch.object(pymport, "print") as printer,
    ):
        result = pymport.do_help()
        assert result is None
        finish.assert_called_once_with(1)
        printer.assert_has_calls(
            (
                unittest.mock.call("pymport.py v.1.0"),
                unittest.mock.call("Detect unused imports."),
                unittest.mock.call("Use a comment like '# noqa: unused-import' to ignore the line."),
                unittest.mock.call(""),
                unittest.mock.call("Usage: pymport.py [--help] [FILE]..."),
                unittest.mock.call(""),
                unittest.mock.call("FILE: File or directory."),
            ),
        )


def test_do_help_header():
    with (
        unittest.mock.patch("pymport.sys.exit") as finish,
        unittest.mock.patch.object(pymport, "print") as printer,
    ):
        result = pymport.do_help(header=("a",))
        assert result is None
        finish.assert_called_once_with(1)
        printer.assert_has_calls(
            (
                unittest.mock.call("a"),
                unittest.mock.call("pymport.py v.1.0"),
                unittest.mock.call("Detect unused imports."),
                unittest.mock.call("Use a comment like '# noqa: unused-import' to ignore the line."),
                unittest.mock.call(""),
                unittest.mock.call("Usage: pymport.py [--help] [FILE]..."),
                unittest.mock.call(""),
                unittest.mock.call("FILE: File or directory."),
            ),
        )
