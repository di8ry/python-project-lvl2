from gendiff.scripts.gendiff import main
import tests.expect as expect


def test_simple_str():
    string = main('simple_before.json', 'simple_after.json', 'json')
    assert string == expect.Simple_string

def test_simple_pl():
    string = main('simple_before.json', 'simple_after.json', 'plain')
    assert string == expect.simple_plain

def test_hard_str():
    string = main('hard_before.json', 'hard_after.json', 'json')
    assert string == expect.Hard_string

def test_hard_pl():
    string = main('hard_before.json', 'hard_after.json', 'plain')
    assert string == expect.Hard_plain

if __name__ == '__main__':
    test_simple_pl()