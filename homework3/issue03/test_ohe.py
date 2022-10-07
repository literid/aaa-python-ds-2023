from one_hot_encoder import fit_transform
import unittest


class TestOhe(unittest.TestCase):
    def test_cities_input(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_identical_input(self):
        word_count = 5
        input_ = ['apple'] * word_count
        actual = fit_transform(input_)
        expected = [('apple', [1]) for _ in range(word_count)]
        self.assertEqual(actual, expected)

    def test_str_input(self):
        actual = fit_transform('apple', 'banana', 'orange')
        expected = [
            ('apple', [0, 0, 1]),
            ('banana', [0, 1, 0]),
            ('orange', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()
