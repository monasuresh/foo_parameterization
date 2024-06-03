#!/user/bin/env python
def validate_is_positive_number(shape_measurement):
    """
    Validate shape properties.

    Parameters:
    parameters (list): The parameters to validate.

    Returns:
    bool: True if all parameters are valid (positive floats), False otherwise.
    """

    return isinstance(shape_measurement, (int, float)) and shape_measurement > 0

