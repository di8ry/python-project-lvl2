from gendiff.generate_diff import difference
import tests.expect as expect


def test_simple_str():
    string = difference('./tests/fixtures/simple_before.json', './tests/fixtures/simple_before.json', 'json')
    assert string == expect.Simple_string

