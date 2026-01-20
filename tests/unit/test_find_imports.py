# -*- coding: utf-8 -*-

import pytest

import pymport
import tests


def test_find_imports_line():
    code = (
        "# -*- coding: utf-8 -*-",
        "import a",
        "",
        "# Comment",
        "import b",
    )
    expected = (
        ("a", 2),
        ("b", 5),
    )
    tree = tests.make_ast(code)
    items = pymport.find_imports(tree)
    result = tuple(items)
    assert result == expected


def test_find_import_from_future():
    code = "from __future__ import absolute_import"
    expected = tuple()
    tree = tests.make_ast(code)
    items = pymport.find_imports(tree)
    result = tuple(items)
    assert result == expected


def test_find_import_star():
    code = "from a import *"
    expected = tuple()
    tree = tests.make_ast(code)
    items = pymport.find_imports(tree)
    result = tuple(items)
    assert result == expected


@pytest.mark.parametrize(
    "code, expected",
    (
        (
            "import a",
            (("a", 1),),
        ),
        (
            "import a, b",
            (("a", 1), ("b", 1)),
        ),
        (
            "import a as a1, b as b1",
            (("a1", 1), ("b1", 1)),
        ),
    ),
)
def test_find_imports(code, expected):
    tree = tests.make_ast(code)
    items = pymport.find_imports(tree)
    result = tuple(items)
    assert result == expected


@pytest.mark.parametrize(
    "code, expected",
    (
        (
            "from a import b",
            (("b", 1),),
        ),
        (
            "from a import b, c",
            (("b", 1), ("c", 1)),
        ),
        (
            "from a import b as b1, c as c2",
            (("b1", 1), ("c2", 1)),
        ),
        (
            "from ..a import b, c as c1",
            (("b", 1), ("c1", 1)),
        ),
    ),
)
def test_find_imports_from(code, expected):
    tree = tests.make_ast(code)
    items = pymport.find_imports(tree)
    result = tuple(items)
    assert result == expected
