from perm_check import MyStr
from string_compression import str_compressed
from is_Unique import is_unique
from one_away import one_away
from perm_palindrome import perm_palindrome
from URLify import urlify


def test_perm_check():
    first = MyStr("bate")
    second = MyStr("beat")

    assert first.is_perm(second) == True


def test_str_compress():

    assert str_compressed("aabcccccaaa") == "a2b1c5a3"
    assert str_compressed("bbbbbbuuffffjjjaattttyyyyjjj") == "b6u2f4j3a2t4y4j3"
    assert str_compressed("abcdefghi") == "abcdefghi"
    assert str_compressed("a/") == None


def test_is_unique():

    assert is_unique("time") == True
    assert is_unique("teenager") == False
    assert is_unique("stream") == True
    assert is_unique("Eagle") == False


def test_one_away():
    assert one_away("pale", "ple") == True
    assert one_away("pain", "rain") == True
    assert one_away("pales", "bakes") == False
    assert one_away("snake", "snail") == False


def test_perm_palindrome():
    assert perm_palindrome("strpau") == False
    assert perm_palindrome("tact coa") == True
    assert perm_palindrome("a") == False
    assert perm_palindrome("jean") == False


def test_urlify():
    assert urlify("Mr John Smith") == "Mr%20John%20Smith"
    assert urlify(" rectify the problem ") == "rectify%20the%20problem"
