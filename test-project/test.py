# Test file for AI Editor
from utils import print_result, get_test_cases, validate_result
from math_utils import calculate_circle_area


def hello_world():
    """Simple function to test AI capabilities"""
    print("Hello from AI Editor!")
    return "Success"


def calculate_operation(a, b, operation="add"):
    """
    Perform an operation (add, multiply, divide) on two numbers.

    Args:
        a (int/float): The first number.
        b (int/float): The second number.
        operation (str): The operation to perform ('add', 'multiply', 'divide').

    Returns:
        int/float: The result of the operation.

    Raises:
        ValueError: If an invalid operation is provided or division by zero occurs.
    """
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError(
            f"Invalid operation: {operation}. Supported operations are 'add', 'multiply', 'divide'."
        )


if __name__ == "__main__":
    hello_world()

    # Test calculate_operation
    test_cases = get_test_cases()
    all_passed = True

    for case in test_cases:
        a = case["a"]
        b = case["b"]
        operation = case["operation"]
        expected_result = case["expected_result"]
        operation_name = case["name"]

        try:
            actual_result = calculate_operation(a, b, operation)
            # Assuming print_result can handle 2 arguments for name and actual_result,
            # or we might need a different print function for single value results.
            # For now, let's adapt its usage.
            print_result(operation_name, a, b, actual_result)
            if not validate_result(actual_result, expected_result, operation_name):
                all_passed = False
        except ValueError as e:
            print(f"Error during {operation_name} of {a} and {b}: {e}")
            print(f"Validation FAILED for {operation_name} due to error.")
            all_passed = False

    # Test calculate_circle_area
    circle_test_cases = [
        {
            "radius": 5,
            "expected_area": 78.53981633974483,
            "name": "Circle area with radius 5",
        },
        {"radius": 0, "expected_area": 0, "name": "Circle area with radius 0"},
        {
            "radius": 2.5,
            "expected_area": 19.634954084936208,
            "name": "Circle area with radius 2.5",
        },
    ]

    # Add a test case for negative radius to test error handling
    try:
        calculate_circle_area(-1)
        print(
            "Validation FAILED for negative radius: Expected ValueError but no error was raised."
        )
        all_passed = False
    except ValueError as e:
        if str(e) == "Radius cannot be negative.":
            print("Validation PASSED for negative radius: Correctly raised ValueError.")
        else:
            print(
                f"Validation FAILED for negative radius: Unexpected error message '{e}'."
            )
            all_passed = False

    for case in circle_test_cases:
        radius = case["radius"]
        expected_area = case["expected_area"]
        test_name = case["name"]

        try:
            actual_area = calculate_circle_area(radius)
            # Using print_result, noting it might be designed for two operands.
            # We'll pass radius as 'a' and None for 'b' if it strictly expects two numbers.
            print_result(test_name, radius, None, actual_area)  # Adapted call
            if not validate_result(actual_area, expected_area, test_name):
                all_passed = False
        except ValueError as e:
            print(f"Error during {test_name} for radius {radius}: {e}")
            print(f"Validation FAILED for {test_name} due to error.")
            all_passed = False
            # If an unexpected error occurs for a valid case, mark as failed
            if radius >= 0:
                all_passed = False

    if all_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed.")
