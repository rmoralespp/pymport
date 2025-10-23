# -*- coding: utf-8 -*-

import ast
import unittest.mock


def make_ast(block):
    if isinstance(block, tuple):
        block = "\n".join(block)
    return ast.parse(block)


ok_call = unittest.mock.call('All checks passed!')
