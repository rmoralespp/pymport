# -*- coding: utf-8 -*-

import pymport
import tests


def test_function_decorator():
    code = (
        "@a",
        "@a.b",
        "@a.b.c()",
        "@a.b.c.d[0]",
        "def function():",
        "    pass",
    )
    expected = (
        ("a",),
        ("a", "a.b"),
        ("a", "a.b", "a.b.c"),
        ("a", "a.b", "a.b.c", "a.b.c.d"),
    )
    tree = tests.make_ast(code)
    items = pymport.find_dotted_names(tree)
    result = tuple(items)
    assert result == expected


def test_class_decorator():
    code = (
        "@a",
        "@a.b",
        "@a.b.c()",
        "@a.b.c.d[0]",
        "class Foo:",
        "    pass",
    )
    expected = (
        ("a",),
        ("a", "a.b"),
        ("a", "a.b", "a.b.c"),
        ("a", "a.b", "a.b.c", "a.b.c.d"),
    )
    tree = tests.make_ast(code)
    items = pymport.find_dotted_names(tree)
    result = tuple(items)
    assert result == expected
