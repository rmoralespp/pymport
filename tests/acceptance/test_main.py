# -*- coding: utf-8 -*-

import pathlib
import tempfile
import unittest.mock

import pymport


def test_main_ok():
    with (
        tempfile.TemporaryDirectory() as tmp,
        unittest.mock.patch("pymport.print") as printer,
    ):
        root = pathlib.Path(tmp)

        item = root / "f1.py"
        item.write_bytes(b"")

        directory = root / "d1"
        directory.mkdir()
        item = directory / "f2.txt"
        item.write_bytes(b"")

        item = directory / "f3.py"
        item.write_bytes(b"")

        context = {"files": [root]}
        result = pymport.main(context)
        assert result == 0
        printer.assert_not_called()


def test_main_errors():
    with (
        tempfile.TemporaryDirectory() as tmp,
        unittest.mock.patch("pymport.print") as printer,
    ):
        root = pathlib.Path(tmp)

        item1 = root / "f1.py"
        item1.write_bytes(
            (
                b"# -*- coding: latin1 -*-\n"
                b"import a\n"
                b"import b # noqa: unused-import\n"
            ),
        )

        directory = root / "d1"
        directory.mkdir()
        item = directory / "f2.txt"
        item.write_bytes(b"")

        item2 = directory / "f3.py"
        item2.write_bytes(b"import b")

        context = {"files": [root]}
        result = pymport.main(context)
        assert result == 1
        printer.assert_has_calls(
            (
                unittest.mock.call("{}:2: a".format(item1)),
                unittest.mock.call("{}:1: b".format(item2)),
            ),
            any_order=True,  # In linux glob does not garantee order
        )


def test_main_syntax_error():
    with (
        tempfile.TemporaryDirectory() as tmp,
        unittest.mock.patch("pymport.print") as printer,
    ):
        root = pathlib.Path(tmp)
        item = root / "f1.py"
        item.write_bytes(b"@!2")

        context = {"files": [root]}
        result = pymport.main(context)
        assert result == 0
        printer.assert_not_called()
