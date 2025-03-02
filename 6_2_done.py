#Task 1
def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type != 'admin':
            raise ValueError("Permission denied")
        return func(*args, **kwargs)
    return wrapper
#Task 2
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__} {e}")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])
#Task 3
def check_types(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        arg_names = func.__code__.co_varnames #Get names of arguments
        # check pos arguments
        for i, arg in enumerate(args):
            if i < len(arg_names):
                param_name = arg_names[i]
                if param_name in annotations:
                    expected_type = annotations[param_name]
                    if not isinstance(arg, expected_type):
                        raise TypeError(f"Argument '{param_name}' must be {expected_type}, got {type(arg)}")
        for param_name, arg in kwargs.items():
            if param_name in annotations:
                expected_type = annotations[param_name]
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument '{param_name}' must be {expected_type}, got {type(arg)}")

        result = func(*args, **kwargs)

        return_type = annotations.get('return')
        if return_type and not isinstance(result, return_type):
            raise TypeError(f"Return value must be {return_type}, got {type(result)}")

        return result

    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b
#Task 4
def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@cache_result
def slow_function(x, y):
    print(f"Выполняется функция с аргументами {x}, {y}")
    return x * y
#Task 5
import time
from collections import deque

def rate_limit(calls_per_min):
    interval = 60 / calls_per_min
    call_times = deque()
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            while call_times and call_times[0] < current_time - 60:
                call_times.popleft()

            if len(call_times) >= calls_per_min:
                wait_time = interval - (current_time - call_times[-1])
                if wait_time > 0:
                    print(f'Rate limit exceeded, waiting {wait_time:.2f} seconds')
                    return None
            call_times.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(5)
def my_func():
    print('Done!')