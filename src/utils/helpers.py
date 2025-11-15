def example_helper_function(param1, param2):
    """
    This is an example helper function that performs a simple operation.
    
    Parameters:
    param1 (int): The first parameter.
    param2 (int): The second parameter.
    
    Returns:
    int: The sum of param1 and param2.
    """
    return param1 + param2

def another_helper_function(data):
    """
    This function processes the input data and returns the result.
    
    Parameters:
    data (list): A list of data points.
    
    Returns:
    list: A list of processed data points.
    """
    # Example processing: return the data squared
    return [x ** 2 for x in data]