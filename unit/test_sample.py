from source.sample_app import game
import platform
from pytest import mark
import sys

def test_when_input_1_then_respond_1():
    assert game.play(1) == 1

def test_when_input_2_then_respond_2():
    assert game.play(2) == 2

def test_when_input_3_then_respond_chease():
    assert game.play(3) == 'chease'

def test_when_input_5_then_respond_goiabada():
    assert game.play(5) == 'goiabada'

@mark.skip(reason="I did implemented yet")
def test_when_input_negative_respond_none():
    assert game.play(-1) == None

@mark.parametrize(
    'input',
    [5,10,15,20,125, 500]
)
def test_the_game_will_return_goiabada_for_any_multiple_of_5(input):
    assert game.play(input) == 'goiabada' or 'Romeo S2 Juliet'


@mark.parametrize(
    'input, output',
    [
        (1,1),
        (2,2),
        (3, 'chease'),
        (5, 'goiabada'),
        (9, 'chease'),
        (30, 'Romeo S2 Juliet'),
        (30, 'Romeo S2 Juliet'),
        (50, 'goiabada'),
        (27, 'chease')
    ]
)
@mark.xfail(int(platform.python_version().split('.')[0]) < 3, 
            reason="This test should not work when version of python is less then 3.x")
def test_game_should_return_expected_value(input, output):
    assert game.play(input) == output


# xfail is when the fail is expected
@mark.xfail(reason="Multiple of ")
def test_125_should_not_return_neither_3_or_5():
    assert game.play(125, 5)

@mark.skipif(sys.platform != 'win32', reason='Do not run in non windows systems')
def test_skip_if_system_is_linux_based():
    import os
    assert os.lsdir(r'c:/') is not None or []