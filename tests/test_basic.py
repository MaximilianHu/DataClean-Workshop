from dclean import main


def test_trim_basic():
    assert __import__('src.cleaners', fromlist=['trim_lines']).trim_lines([' a ','b  ']) == ['a','b']


def test_unique_basic():
    assert __import__('src.cleaners', fromlist=['unique_lines']).unique_lines(['a','a','b']) == ['a','b']
from src.textutils import normalize_email, is_valid_email


def test_normalize_email():
    assert normalize_email('  Foo@Example.COM ') == 'foo@example.com'


def test_is_valid_email():
    assert is_valid_email('a@b.co')
    assert not is_valid_email('bad@@ex')
