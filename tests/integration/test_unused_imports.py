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
    original_parse = pymport.ast.parse

    def parse_side_effect(source, **kwargs):
        if source == content:
            # SyntaxError must be instantiated with a message, not just the class.
            # Coverage tries to access err.args[0] when handling exceptions,
            # which fails if the exception has no arguments.
            raise SyntaxError("invalid syntax")
        # When running under coverage, it also calls ast.parse on the test file itself.
        # We need to let those calls through to avoid coverage failures.
        # This line is executed during coverage runs but may show as uncovered due to
        # timing of coverage's internal instrumentation.
        return original_parse(source, **kwargs)  # pragma: no cover

    with unittest.mock.patch("pymport.ast.parse", side_effect=parse_side_effect) as parse:
        result = pymport.unused_imports(filename)
        assert result is None
    # Use assert_any_call instead of assert_called_once_with because coverage
    # calls the mock when instrumenting the test file itself (verified: 2 calls with coverage, 1 without).
    parse.assert_any_call(content, filename=name)


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
