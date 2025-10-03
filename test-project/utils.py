# Utility functions for the test project


def print_result(operation_name, a, b, result):
    """
    Prints the result of a calculation in a formatted way.

    Args:
        operation_name (str): The name of the operation (e.g., "Addition", "Multiplication").
        a (int/float): The first number.
        b (int/float): The second number.
        result (int/float): The result of the operation.
    """
    print(f"{operation_name} of {a} and {b} is: {result}")


def get_test_cases():
    """
    Provides a list of test cases for the calculate_operation function.
    Each test case is a dictionary with 'a', 'b', 'operation', and 'expected_result'.

    Returns:
        list: A list of test case dictionaries.
    """
    return [
        {
            "a": 10,
            "b": 5,
            "operation": "add",
            "expected_result": 15,
            "name": "Addition",
        },
        {
            "a": 10,
            "b": 5,
            "operation": "multiply",
            "expected_result": 50,
            "name": "Multiplication",
        },
        {
            "a": 20,
            "b": 4,
            "operation": "divide",
            "expected_result": 5.0,
            "name": "Division",
        },
        {
            "a": 7,
            "b": 3,
            "operation": "multiply",
            "expected_result": 21,
            "name": "Another Multiplication",
        },
        {
            "a": 0,
            "b": 0,
            "operation": "add",
            "expected_result": 0,
            "name": "Zero Addition",
        },
    ]


def validate_result(actual, expected, operation_name):
    """
    Validates if the actual result matches the expected result.

    Args:
        actual (int/float): The actual result from the function.
        expected (int/float): The expected result.
        operation_name (str): The name of the operation for error messages.

    Returns:
        bool: True if results match, False otherwise.
    """
    if actual == expected:
        print(f"Validation successful for {operation_name}.")
        return True
    else:
        print(
            f"Validation FAILED for {operation_name}. Expected: {expected}, Got: {actual}"
        )
        return False
