# -*- coding: utf-8 -*-

import ast


def make_ast(block):
    if isinstance(block, tuple):
        block = "\n".join(block)
    return ast.parse(block)
