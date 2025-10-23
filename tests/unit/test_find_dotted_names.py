# -*- coding: utf-8 -*-

import pymport
import tests


def test_find_dotted_names_not_name_after_attribute():
    expected = (
        ("foo",),
        ("bar",),
    )
    code = "foo = bar(1).zas"
    tree = tests.make_ast(code)
    items = pymport.find_dotted_names(tree)
    result = tuple(items)
    assert result == expected


def test_find_dotted_names():
    code = (
        "a",
        "a.b",
        "a.b.c",
        "f'{a.b}'",
    )
    expected = (
        ("a",),
        ("a", "a.b"),
        ("a", "a.b", "a.b.c"),
    )
    tree = tests.make_ast(code)
    items = pymport.find_dotted_names(tree)
    result = tuple(items)
    assert result == expected
