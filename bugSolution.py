def function_with_robust_error_handling(a, b):
    try:
        if isinstance(b, (str, list, tuple)):
            raise TypeError("Cannot divide by string, list or tuple")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

#Corrected code for the nested function
def outer_function_corrected():
    x = 10
    def inner_function():
        y = 20
        #Accessing z within its scope
        return x/z
    z = 5
    return inner_function()

result1 = function_with_robust_error_handling(10, "abc")
print(f"Result 1: {result1}") #Output: Error: Cannot divide by string, list or tuple Result 1: None
result2 = function_with_robust_error_handling(10, 2)
print(f"Result 2: {result2}") #Output: Result 2: 5.0
result3 = outer_function_corrected()
print(f"Result 3: {result3}") #Output: Result 3: 2.0