#!/user/bin/env python
"""
CommandLineInterface Module

This module provides a command-line interface (CLI) for interacting with the FooParameterization class
to calculate volumes of various shapes.

Classes:
    CommandLineInterface: A command-line interface class for interacting with shape parameterization.

Usage:
    $ python foo_parameterization_cli.py

    The user will be prompted to select a shape and provide necessary parameters (e.g., radius).
    The CLI then calculates and displays the volume of the selected shape using FooParameterization.

Author:
    Monica Suresh

Date:
    06/03/2024

"""

# Now try the absolute import
from foo.foo_parameterization_core import FooParameterization
from foo import validation


class CommandLineInterface:
    """
    CommandLineInterface Class

    A command-line interface class for interacting with shape parameterization.

    Methods:
        get_shape_property(): Prompt the user to select a shape property (e.g., volume).
        get_shape(): Prompt the user to select a shape (e.g., sphere).
        get_parameter(parameter_name, parameter_type): Prompt the user to input a parameter of a specified type.
        run(): Run the CLI, prompting the user for inputs and calculating the volume of the selected shape.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_shape_property():
        """
        Prompt the user to select a shape property.

        Returns:
            str: The selected shape property.
        """
        shape_properties = {
            1: 'volume'
        }

        print("Available shape properties:")

        for idx, shape_property in shape_properties.items():
            print(f"{idx}. {shape_property}")

        valid_shape_property_choices = ", ".join(map(str, shape_properties.keys()))

        while True:
            try:
                shape_property_choice = int(input(f"Enter the number corresponding to the shape property"
                                                  f"({valid_shape_property_choices}): "))
                if shape_property_choice in shape_properties:
                    return shape_properties[shape_property_choice]
                else:
                    print(f"Please enter one of the following numbers: {valid_shape_property_choices}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    @staticmethod
    def get_shape():
        """
        Prompt the user to select a shape.

        Returns:
            str: The selected shape.
        """
        shapes = {
            1: 'sphere'
        }

        print("Available shapes:")

        for idx, shape in shapes.items():
            print(f"{idx}. {shape}")

        valid_shape_choices = ", ".join(map(str, shapes.keys()))

        while True:
            try:
                shape_choice = int(input(f"Enter the number corresponding to the shape ({valid_shape_choices}): "))
                if shape_choice in shapes:
                    return shapes[shape_choice]
                else:
                    print(f"Please enter one of the following numbers: {valid_shape_choices}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    @staticmethod
    def get_parameter(parameter_name, parameter_type):
        """
        Prompt the user to input a parameter of a specified type.

        Parameters:
            parameter_name (str): The name of the parameter.
            parameter_type (type): The type of the parameter.

        Returns:
            Any: The input parameter of the specified type.
        """
        while True:
            try:
                value = parameter_type(input(f"Enter the {parameter_name}: "))
                return value
            except ValueError:
                print(f"Invalid input. Please enter a valid {parameter_type.__name__}.")

    def run(self):
        """
        Run the command-line interface.

        This method prompts the user for inputs, calculates the volume of the selected shape
        using FooParameterization, and displays the result.
        """
        shape_property = self.get_shape_property()
        shape = self.get_shape()
        foo = FooParameterization()
        volume = None

        if shape == 'sphere' and shape_property == 'volume':
            radius = self.get_parameter('radius', float)
            while not validation.validate_is_positive_number(radius):
                print("Please enter a positive number for the radius.")
                radius = self.get_parameter('radius', float)
            volume = foo.calculate_volume(shape, radius)
        else:
            print(
                f"Calculating the {shape_property} of {shape} with parameterization is not yet supported by Foo et al.")

        if volume:
            print(f"Volume of {shape} with given dimensions: {volume}")



if __name__ == "__main__":
    cli = CommandLineInterface()
    cli.run()
