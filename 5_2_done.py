from typing import List, Callable
#Task 1
def apply(li: List[int], func: Callable[[int], int]) -> List[int]:
    for i in range(len(li)):
        li[i] = func(li[i])
    return li
a = [1, 2, 3]
def times_2(num: int) -> int:
    return num * 2
apply(a, times_2)
print(a)  # should print [2, 4, 6]
#Task 2
b = [4, 5, 6]
apply(b, lambda num: num * 2)
print(b)  # should print [8, 10, 12]
#Task 3
def sum_even(li: List[int]) -> List[int]:
    def is_even(num: int) -> bool:
        return num % 2 == 0
    return sum(x for x in li if is_even(x))
#Task 4
import datetime
def add_logging(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
        print(f"Function `{func.__name__}` called at {time}")
        return func(*args, **kwargs)
    return wrapper

def my_func(num: int) -> int:
    return 0.1 * num ** 2

my_func_with_log = add_logging(my_func)

print(my_func_with_log(5))

# should print something like:
# function `my_func` called at 2024-01-26T14:30:00Z
# 2.5

#Task 5
@add_logging
def some_function():
    pass

some_function()
# should print something like:
# function `some_function` called at 2024-01-26T14:30:00Z