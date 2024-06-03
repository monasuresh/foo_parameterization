import pytest
from unittest.mock import patch
from foo.foo_parameterization_cli import CommandLineInterface
from foo.foo_parameterization_core import FooParameterization


@patch('builtins.input', side_effect=['1'])
def test_get_shape_property_valid_input(mock_input):
    cli = CommandLineInterface()
    result = cli.get_shape_property()
    assert result == 'volume'


@patch('builtins.input', side_effect=['invalid', '2', '1'])
def test_get_shape_property_invalid_then_valid_input(mock_input):
    cli = CommandLineInterface()
    result = cli.get_shape_property()
    assert result == 'volume'


@patch('builtins.input', side_effect=['1'])
def test_get_shape_valid_input(mock_input):
    cli = CommandLineInterface()
    result = cli.get_shape()
    assert result == 'sphere'


@patch('builtins.input', side_effect=['invalid', '2', '1'])
def test_get_shape_invalid_then_valid_input(mock_input):
    cli = CommandLineInterface()
    result = cli.get_shape()
    assert result == 'sphere'


@patch('builtins.input', side_effect=['3.5'])
def test_get_parameter_valid_float(mock_input):
    cli = CommandLineInterface()
    result = cli.get_parameter('radius', float)
    assert result == 3.5


@patch('builtins.input', side_effect=['invalid', '3.5'])
def test_get_parameter_invalid_then_valid_float(mock_input):
    cli = CommandLineInterface()
    result = cli.get_parameter('radius', float)
    assert result == 3.5


@patch('builtins.input', side_effect=['2'])
@patch.object(FooParameterization, 'calculate_volume', return_value=33.51)
def test_run_sphere_volume(mock_calculate_volume, mock_input):
    cli = CommandLineInterface()
    cli.get_shape_property = lambda: 'volume'
    cli.get_shape = lambda: 'sphere'
    cli.get_parameter = lambda name, ptype: 2.0
    with patch('builtins.print') as mock_print:
        cli.run()
        mock_print.assert_any_call('Volume of sphere with given dimensions: 33.51')


@patch('builtins.input', side_effect=['2'])
@patch.object(FooParameterization, 'calculate_volume', return_value=None)
def test_run_unsupported_shape(mock_calculate_volume, mock_input):
    cli = CommandLineInterface()
    cli.get_shape_property = lambda: 'volume'
    cli.get_shape = lambda: 'unsupported_shape'
    with patch('builtins.print') as mock_print:
        cli.run()
        mock_print.assert_any_call('Calculating the volume of unsupported_shape with parameterization is not yet '
                                   'supported by Foo et al.')
