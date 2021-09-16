import pytest
from pathfind_a_star import Mapa

def test_basic_pathfind():
    mapa = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 2],
    ]
    result = \
        "o  \n" \
        " o \n" \
        "  X\n"
    a = Mapa(mapa)
    a.resolve()

    assert result == str(a)

def test_obstacle():
    mapa = [
        [1, 3, 0],
        [0, 3, 0],
        [0, 0, 2],
    ]
    result = \
        "o| \n" \
        "o| \n" \
        " oX\n"
    a = Mapa(mapa)
    a.resolve()

    assert result == str(a)

    mapa = [
        [1, 3, 0],
        [0, 3, 0],
        [3, 0, 2],
    ]
    result = \
        "o| \n" \
        "o| \n" \
        "|oX\n"
    a = Mapa(mapa)
    a.resolve()

    assert result == str(a)

def test_complex():
    mapa = [
        [1, 3, 3, 0 , 0, 0, 0, 0],
        [0, 3, 0, 0 , 0, 3, 3, 0],
        [3, 0, 3, 3 , 3, 0, 3, 0],
        [3, 3, 3, 0 , 0, 3, 3, 0],
        [0, 0, 0, 0 , 0, 3, 0, 0],
        [0, 0, 0, 0 , 0, 0, 3, 2],
    ]
    result = \
        "o||     \n"\
        "o|ooo|| \n"\
        "|o|||o| \n"\
        "||| o|| \n"\
        "    o|o \n"\
        "     o|X\n"
    a = Mapa(mapa)
    a.resolve()

    assert result == str(a)

@pytest.mark.skip('FIXME')
def test_complex_fail():
    mapa = [
        [1, 3, 3, 0 , 0, 0, 0, 0],
        [0, 3, 0, 0 , 0, 3, 3, 0],
        [3, 0, 3, 3 , 3, 0, 3, 0],
        [3, 3, 3, 0 , 0, 3, 3, 0],
        [0, 0, 0, 0 , 0, 3, 3, 0],
        [0, 0, 0, 0 , 0, 0, 3, 2],
    ]
    result = \
        "o||     \n"\
        "o|ooo|| \n"\
        "|o|||o| \n"\
        "||| o|| \n"\
        "    o|o \n"\
        "     o|X\n"
    a = Mapa(mapa)
    a.resolve()

    assert result == str(a)