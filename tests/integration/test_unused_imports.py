# -*- coding: utf-8 -*-

import unittest.mock

import pytest

import pymport


def test_unused_imports_syntax_error():
    content = b""
    name = "foo"
    filename = unittest.mock.Mock()
    filename.__str__ = unittest.mock.MagicMock(return_value=name)
    filename.read_bytes = unittest.mock.Mock(return_value=content)
    with unittest.mock.patch("pymport.ast.parse", side_effect=SyntaxError) as parse:
        result = pymport.unused_imports(filename)
        assert result is None
        parse.assert_called_once_with(content, filename=name)


def test_unused_imports_empty():
    name = "foo"
    filename = unittest.mock.Mock()
    filename.__str__ = unittest.mock.MagicMock(return_value=name)
    filename.read_bytes = unittest.mock.Mock(return_value=b"")
    with unittest.mock.patch("pymport.linecache.getline") as getline:
        result = pymport.unused_imports(filename)
        assert result is None
        getline.assert_not_called()


def test_unused_imports():
    code = (
        b"# -*- coding: utf-8 -*-",
        b"import a",
        b"import b",
        b"a.b",
        b"x.y.z()",
    )
    name = "foo"
    expected = (
        (name, 3, "b"),
    )
    filename = unittest.mock.Mock()
    filename.__str__ = unittest.mock.MagicMock(return_value=name)
    filename.read_bytes = unittest.mock.Mock(return_value=b"\n".join(code))
    with unittest.mock.patch("pymport.linecache.getline", return_value="") as getline:
        result = pymport.unused_imports(filename)
        assert result == expected
        getline.assert_called_once_with(name, 3)


@pytest.mark.parametrize(
    "noqa",
    (
        "# noqa",
        "# noqa: F401",
        "# noqa:  F401  ",
    ),
)
def test_unused_imports_filtered(noqa):
    code = (
        b"# -*- coding: utf-8 -*-",
        b"import a",
        b"import b",
        b"import c",
        b"a.b",
        b"x.y.z()",
    )

    ignore = noqa
    name = "foo"
    expected = None
    filename = unittest.mock.Mock()
    filename.__str__ = unittest.mock.MagicMock(return_value=name)
    filename.read_bytes = unittest.mock.Mock(return_value=b"\n".join(code))
    with unittest.mock.patch("pymport.linecache.getline", return_value=ignore) as getline:
        result = pymport.unused_imports(filename)
        assert result == expected
        getline.assert_has_calls(
            (
                unittest.mock.call(name, 3),
                unittest.mock.call(name, 4),
            ),
        )
