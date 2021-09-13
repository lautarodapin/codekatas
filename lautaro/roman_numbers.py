# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from typing import *


# %%

class RomanToDecimal:
    letters = dict(i=1, v=5, x=10, l=50, c=100, d=500, m=1000)
    total: int
    roman_number: str

    def __init__(self, roman_number: str) -> None:
        self.roman_number = roman_number.lower()
        self.number_list = [self.letters[letter] for letter in self.roman_number]
        self.resolve()

    def __repr__(self) -> str:
        return f'{self.roman_number.upper()} = {self.suma}'

    def __getitem__(self, index) -> Optional[int]:
        try:
            return self.number_list[index]
        except IndexError:
            return None

    def __iter__(self) -> Iterator[Tuple[int, Optional[int]]]:
        for i, curr in enumerate(self.number_list):
            yield curr, self[i+1] 

    def resolve(self):
        self.suma = sum([curr if next is None or curr >= next else -curr for curr, next in self])


# %%
RomanToDecimal('XXIV')


# %%
class DecimalToRoman:
    number: int
    roman_number: str = ''
    numbers = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl',
        50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    def __init__(self, number: int) -> None:
        self.number = number
        self.resolve()
        
    def __repr__(self) -> str:
        return f'{self.number} = {self.roman_number}'

    def __iter__(self) -> Iterator[Tuple[int, str]]:
        for k, v in reversed(self.numbers.items()):
            yield k, v

    def resolve(self):
        total = self.number
        self.roman_number = ''
        while total > 0:
            for number, letter in self:
                if total / number >= 1:
                    total -= number
                    self.roman_number += letter.upper()
                    break


# %%
DecimalToRoman(49)


# %%
class RomanToDecimal2:
    letters: Dict[str, int] = dict(i=1, iv=4, v=5, ix=9, x=10, xl=40, l=50, xc=90, c=100, cd=400, d=500, cm=900, m=1000)

    def __init__(self, roman_number: str) -> None:
        self.roman_number = roman_number.lower()
        self.resolve()

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'{self.roman_number.upper()} = {self.result}'

    def __iter__(self) -> Iterator[Tuple[Optional[str], str, Optional[str]]]:
        for i, curr in enumerate(self.roman_number):
            yield self[i-1], curr, self[i+1] 

    def __getitem__(self, index) -> Optional[str]:
        try:
            if index >= 0:
                return self.roman_number[index]
        except IndexError:
            return None

    def resolve(self) -> int:
        string = ''
        for previous_letter, letter, next_letter in self:
            if letter and next_letter and letter + next_letter in self.letters:
                continue
            if previous_letter and letter and previous_letter + letter in self.letters:
                string += 'i' * self.letters[previous_letter + letter]
                continue
            string += 'i' * self.letters[letter]
        self.result = len(string)
        return self.result
