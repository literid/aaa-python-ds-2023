import pytest
from morse_decode import decode


@pytest.mark.parametrize(
    'morse_msg, decoded_msg',
    [
        ('... --- ...', 'SOS'),
        ('.- .--. .--. .-.. .', 'APPLE'),
        ('.-.-.- .---- -....- ..--- -....- ----- .-.-.-', '.1-2-0.')
    ]
)
def test_decode(morse_msg: str, decoded_msg: str):
    assert decode(morse_msg) == decoded_msg
