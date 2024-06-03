import pytest
from unittest.mock import patch
import math
from foo.foo_parameterization_core import FooParameterization

@patch('foo.foo_parameterization_core.validation.validate_is_positive_number', return_value=True)
def test_calculate_volume_sphere(mock_validation):
    radius = 3.0
    expected_volume = 4 / 3 * math.pi * radius ** 3
    result = FooParameterization.calculate_volume('sphere', radius)
    assert result == pytest.approx(expected_volume, rel=1e-5)

@patch('foo.foo_parameterization_core.validation.validate_is_positive_number', return_value=False)
def test_calculate_volume_sphere_negative_radius(mock_validation):
    radius = -3.0
    with pytest.raises(ValueError) as exc_info:
        FooParameterization.calculate_volume('sphere', radius)
    assert str(exc_info.value) == "Radius must be a positive number"

def test_calculate_volume_unsupported_shape():
    with pytest.raises(ValueError) as exc_info:
        FooParameterization.calculate_volume('cube', 3.0)
    assert str(exc_info.value) == "Shape cube is not supported"

def test_triple_integral_integrand_sphere():
    x, y, z = 1, 1, math.pi / 2
    expected_result = z ** 2 * math.sin(x)
    result = FooParameterization.triple_integral_integrand(x, y, z, "sphere")
    assert result == expected_result

def test_triple_integral_integrand_invalid_shape():
    x, y, z = 1, 1, math.pi / 2
    with pytest.raises(ValueError) as exc_info:
        FooParameterization.triple_integral_integrand(x, y, z, "cube")
    assert str(exc_info.value) == "Shape cube is not supported in the integrand"

@patch('scipy.integrate.tplquad', return_value=(113.097, 0))
def test_calculate_volume_of_sphere(mock_tplquad):
    radius = 3.0
    result = FooParameterization.calculate_volume_of_sphere(radius)
    expected_volume = 113.097  # Volume calculated by tplquad mock
    assert result == pytest.approx(expected_volume, rel=1e-3)

def test_calculate_volume_of_invalid_radius_type():
    with pytest.raises(ValueError) as exc_info:
        FooParameterization.calculate_volume('sphere', 'abc')
    assert str(exc_info.value) == "Radius must be a positive number"

def test_calculate_volume_of_sphere_zero_radius():
    radius = 0.0
    with pytest.raises(ValueError) as exc_info:
        FooParameterization.calculate_volume('sphere', radius)
    assert str(exc_info.value) == "Radius must be a positive number"
