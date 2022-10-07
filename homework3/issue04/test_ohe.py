from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    'input_, expected_out',
    [
        (['Moscow', 'New York', 'Moscow', 'London'], [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]),
        (['apple'] * 5, [
            ('apple', [1]) for _ in range(5)
        ])
    ]
)
def test_different_inputs(input_, expected_out):
    actual = fit_transform(input_)
    assert actual == expected_out


def test_str_input():
    actual = fit_transform('apple', 'banana', 'orange')
    expected = [
        ('apple', [0, 0, 1]),
        ('banana', [0, 1, 0]),
        ('orange', [1, 0, 0])
    ]
    assert actual == expected


def test_empty_input():
    with pytest.raises(TypeError):
        fit_transform()
