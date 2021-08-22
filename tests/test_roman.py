import pytest
from collections import namedtuple
from roman_numbers import RomanToDecimal, DecimalToRoman

RomanToDecimalTest = namedtuple('RomanToDecimalTest', 'roman_number number')


def test_roman_to_decimal():
    for test_value in TEST_VALUES:
        result = RomanToDecimal(test_value.roman_number)
        assert result.suma == test_value.number

def test_decimal_to_roman():
    for test_value in TEST_VALUES:
        result = DecimalToRoman(test_value.number)
        assert result.roman_number == test_value.roman_number

TEST_VALUES = [
    RomanToDecimalTest('I', 1),
    RomanToDecimalTest('II', 2),
    RomanToDecimalTest('III', 3),
    RomanToDecimalTest('IV', 4),
    RomanToDecimalTest('V', 5),
    RomanToDecimalTest('VI', 6),
    RomanToDecimalTest('IX', 9),
    RomanToDecimalTest('X', 10),
    RomanToDecimalTest('XII', 12),
    RomanToDecimalTest('XV', 15),
    RomanToDecimalTest('XXIV', 24),
    RomanToDecimalTest('XXV', 25),
    RomanToDecimalTest('XXXVII', 37),
    RomanToDecimalTest('CIV', 104),
    RomanToDecimalTest('M', 1000),
    RomanToDecimalTest('MMMCMXCIX', 3999),
]