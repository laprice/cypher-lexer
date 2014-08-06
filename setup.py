#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'cypher-lexer',
    version = '0.1',
    description = 'A Pygments lexer for the cypher query language',
    author_email = 'larry@industrialintellect.com',
    url = 'https://github.com/laprice/cypher-lexer',
    install_requires = 'pygments >= 1.5',
    entry_points = { 'pygments.lexers' : '.cyp = cypher.CypherLexer' }
)
