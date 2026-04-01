#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division, or None if division by zero occurs.
    """
    div_result = None
    try:
        div_result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(div_result))
        return div_result
