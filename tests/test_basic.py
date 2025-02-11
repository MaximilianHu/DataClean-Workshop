from dclean import main


def test_trim_basic():
    assert __import__('src.cleaners', fromlist=['trim_lines']).trim_lines([' a ','b  ']) == ['a','b']


def test_unique_basic():
    assert __import__('src.cleaners', fromlist=['unique_lines']).unique_lines(['a','a','b']) == ['a','b']
