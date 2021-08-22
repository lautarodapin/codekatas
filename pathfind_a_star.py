# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from enum import Enum
from dataclasses import dataclass
from typing import *

@dataclass
class Coordinate:
    i: int
    j: int


class State(Enum):
    start = 1
    empty = 0
    end = 2
    obstacle = 3
    path = 4

    @classmethod
    def int_to_state(cls, number: int):
        return rsl[0] if len(rsl:=[state for state in State if state.value == number]) > 0 else None

mapa = [
    [1, 3 , 0, 0,  0],
    [0, 3 , 0, 0,  2],
    [0, 0 , 0, 0,  0],
]


# %%
class Nodo:
    distance_to_end: int
    gain: int
    parent = None #  type: Node
    def __init__(self, state: State, coordinate: Coordinate, end: Coordinate) -> None:
        self.state = state
        self.coordinate = coordinate
        self.end = end
        self.calculate(end)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'''Nodo ({self.coordinate}),\t{self.state.name}={self.state},\tG={self.distance_to_end})'''

    def calculate(self, coordinate: Coordinate) -> int:
        self.distance_to_end = (
            abs(self.coordinate.i - coordinate.i)**2 
            + abs(self.coordinate.j - coordinate.j)**2
        )
        
    def __lt__(self, other):
        return self.distance_to_end < other.distance_to_end

    def __le__(self, other):
        return self.distance_to_end <= other.distance_to_end

    def __eq__(self, other):
        return self.distance_to_end == other.distance_to_end

    def __ne__(self, other):
        return self.distance_to_end != other.distance_to_end

    def __gt__(self, other):
        return self.distance_to_end > other.distance_to_end

    def __ge__(self, other):
        return self.distance_to_end >= other.distance_to_end

class Mapa:
    mapa: List[List[Nodo]]

    def __init__(self, mapa: List[List[int]]) -> None:
        for i, row in enumerate(mapa):
            for j, cell in enumerate(row):
                if State.int_to_state(cell) == State.start:
                    self.init = Coordinate(i=i, j=j)
                elif State.int_to_state(cell) == State.end:
                    self.end = Coordinate(i=i, j=j)
        self.mapa = [
            [
                Nodo(state=State.int_to_state(cell), coordinate=Coordinate(i, j), end=self.end) 
                for j, cell in enumerate(row)
            ] 
            for i, row in enumerate(mapa)
        ]
        self.init = self.mapa[self.init.i][self.init.j]
        self.end = self.mapa[self.end.i][self.end.j]

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        rsl = ''
        for row in self.mapa:
            for cell in row:
                rsl += f'{cell.state}\t'
            rsl += '\n'
        return rsl
    
    def __getitem__(self, index: Tuple[int, int]) -> Optional[Nodo]:
        i, j = index
        if i < 0 or j < 0: return None
        try:
            rsl =  self.mapa[i][j]
            if rsl.state == State.obstacle:
                return None
            return rsl
        except IndexError:
            return None


    def print(self):
        for row in self.mapa:
            print([cell.state.value for cell in row])
        print('\n')

    def calculate(self, nodo: Nodo) -> Optional[Nodo]:
        surroundings = [
            self[nodo.coordinate.i+1, nodo.coordinate.j],
            self[nodo.coordinate.i-1, nodo.coordinate.j],
            self[nodo.coordinate.i, nodo.coordinate.j+1],
            self[nodo.coordinate.i, nodo.coordinate.j-1],
            self[nodo.coordinate.i+1, nodo.coordinate.j+1],
            self[nodo.coordinate.i+1, nodo.coordinate.j-1],
            self[nodo.coordinate.i-1, nodo.coordinate.j-1],
            self[nodo.coordinate.i-1, nodo.coordinate.j+1],
        ]
        _next: Nodo = min(filter(lambda x: x is not None, surroundings))
        _next.parent = nodo
        return _next

    def resolve(self):
        curr = self.init
        while True:
            curr.state = State.path
            curr = self.calculate(curr)
            print(self)
            if curr.state == State.end:
                break


# %%
a = Mapa(mapa)
a.resolve()


# %%



