def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Uncommon Error Scenario: Trying to divide by a string that cannot be implicitly converted
result = function_with_uncommon_error(10, "abc")
print(f"Result: {result}")  # Output: Error: Unsupported operand type(s) for / Result: None

# Another Uncommon Error Scenario:  Trying to divide by a list, causing a TypeError
result = function_with_uncommon_error(10, [1,2,3])
print(f"Result: {result}") # Output: Error: Unsupported operand type(s) for / Result: None

# Uncommon Error Scenario: A nested function with incorrect variable scoping which results in a NameError
def outer_function():
    x = 10
    def inner_function():
        y = 20
        #Uncommon error case: Accessing z outside of its scope
        result = x/z
        return result
    z = 5
    return inner_function()

result = outer_function()
print(f"Result: {result}") # Output: UnboundLocalError: local variable 'z' referenced before assignment