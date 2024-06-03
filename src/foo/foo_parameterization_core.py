#!/user/bin/env python
"""
FooParameterization Module

This module provides functionality for calculating volumes of various shapes using parameterization.

Classes:
    FooParameterization: A class for calculating volumes of shapes using parameterization.

Author:
    Monica Suresh

Date:
    06/03/2024

"""

# Now try the absolute import
from foo import validation
from scipy.integrate import tplquad
from numpy import pi, sin


class FooParameterization:
    """
    FooParameterization Class

    A class for calculating volumes of shapes using parameterization.

    Methods:
        calculate_volume(shape, *args): Calculate the volume of the passed-in shape.
        triple_integral_integrand(x, y, z, shape): Define the integrand function for a triple integral in 3D space.
        calculate_volume_of_sphere(radius): Calculate the volume of a sphere.
    """

    @staticmethod
    def calculate_volume(shape, *args):
        """
        Calculate the volume of the passed-in shape.

        Parameters:
            shape (str): The type of the shape.
            *args: Variable length argument list for shape parameters.

        Returns:
            float: The volume of the passed-in shape.

        Raises:
            ValueError: If the specified shape is not supported or parameters are invalid.
        """
        shape = shape.lower()

        if shape == "sphere":
            radius = args[0]

            if not validation.validate_is_positive_number(radius):
                raise ValueError("Radius must be a positive number")
            return FooParameterization.calculate_volume_of_sphere(radius)
        else:
            raise ValueError(f"Shape {shape} is not supported")

    @staticmethod
    def triple_integral_integrand(x, y, z, shape):
        """
        Define the integrand function for a triple integral in three-dimensional space.

        This function computes the integrand for a triple integral in three-dimensional space
        based on the specified shape.

        Parameters:
            x (float): The value of the x-coordinate.
            y (float): The value of the y-coordinate.
            z (float): The value of the z-coordinate.
            shape (str): The shape for which the integrand is defined.

        Returns:
            float: The value of the integrand at the specified coordinates.

        Raises:
            ValueError: If the specified shape is not supported.
        """
        if shape == "sphere":
            return z ** 2 * sin(x)
        else:
            raise ValueError(f"Shape {shape} is not supported in the integrand")

    @staticmethod
    def calculate_volume_of_sphere(radius):
        """
        Calculate the volume of a sphere.

        Parameters:
            radius (float): The radius of the sphere.

        Returns:
            float: The volume of the sphere.
        """

        # Limits for theta
        t1 = 0
        t2 = 2 * pi

        # Limits for phi
        p1 = 0
        p2 = pi

        # Closure to bind the shape to the integrand
        def integrand_for_sphere(x, y, z):
            return FooParameterization.triple_integral_integrand(x, y, z, "sphere")

        # Calculate the volume of the sphere
        volume = tplquad(integrand_for_sphere, 0, radius, lambda r: t1, lambda r: t2,
                         lambda r, t: p1, lambda r, t: p2)[0]

        return volume
