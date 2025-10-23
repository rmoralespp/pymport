# -*- coding: utf-8 -*-

import pathlib
import tempfile
import unittest.mock

import pymport


def test_walker_is_dir_is_file():
    filename = unittest.mock.Mock()
    filename.is_file = unittest.mock.Mock(return_value=False)
    filename.is_dir = unittest.mock.Mock(return_value=False)

    result = tuple(pymport.walker((filename,)))
    assert not result


def test_walker():
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        expected = sorted(
            (
                root / "f1.py",
                root / "f2.pyw",
                root / "d1" / "f4.py",
                root / "d1" / "f4.py",
            ),
        )

        directory = root / "__pycache__"
        directory.mkdir()
        item = directory / "f1.py"

        item = root / "f1.py"
        item.write_bytes(b"")

        item = root / "f2.pyw"
        item.write_bytes(b"")

        item = root / "f3.txt"
        item.write_bytes(b"")

        directory = root / "d1"
        directory.mkdir()
        item = directory / "f2.txt"
        item.write_bytes(b"")

        item = directory / "f4.py"
        item.write_bytes(b"")

        items = pymport.walker((root, item))
        result = sorted(items)
        assert result == expected
