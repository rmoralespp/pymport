# -*- coding: utf-8 -*-

import pytest

import pymport
import tests


@pytest.mark.parametrize(
    "code, expected",
    (
        (
            "import a",
            (
                ("a", {"names": ("a",), "lineno": 1}),
            ),
        ),
        (
            "import a, b",
            (
                ("a", {"names": ("a",), "lineno": 1}),
                ("b", {"names": ("b",), "lineno": 1}),
            ),
        ),
        (
            "import a as a1, b as b1",
            (
                ("a", {"names": ("a1",), "lineno": 1}),
                ("b", {"names": ("b1",), "lineno": 1}),
            ),
        ),
    ),
)
def test_import_finder(code, expected):
    tree = tests.make_ast(code)
    finder = pymport.ImportFinder()
    finder.visit(tree)
    result = tuple(finder)
    assert result == expected


@pytest.mark.parametrize(
    "code, expected",
    (
        (
            "from a import b",
            (
                ("a", {"names": ("b",), "lineno": 1}),
            ),
        ),
        (
            "from a import b, c",
            (
                ("a", {"names": ("b", "c"), "lineno": 1}),
            ),
        ),
        (
            "from a import b as b1, c as c1",
            (
                ("a", {"names": ("b1", "c1"), "lineno": 1}),
            ),
        ),
        (
            "from ..a import b, c as c1",
            (
                ("a", {"names": ("b", "c1"), "lineno": 1}),
            ),
        ),
    ),
)
def test_import_finder_from(code, expected):
    tree = tests.make_ast(code)
    finder = pymport.ImportFinder()
    finder.visit(tree)
    result = tuple(finder)
    assert result == expected
