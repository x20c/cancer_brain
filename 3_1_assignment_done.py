#Task 1
print('Task 1')
call_counter = 0

def calculate(a, b):
    global call_counter
    call_counter += 1
    return a ** (b / 2)


for _ in range(5):
    calculate(5, 5)

print(f'calculate called {call_counter} times')

#Task 2
print('Task 2')
"""
#a raise SyntaxError
while True print('Hello world')
#b raise ValueError
int('hello')
#c raise NameError
print(debug)
"""
#Task 3
print('Task 3')
a1 = (1, 2, 3, 4, 5)

b1 = (5, 4, 3, 2, 1)

print(b1)  # should print (5, 4, 3, 2, 1)

#Task 4
print('Task 4')
def pop_element(v1: tuple, i: int) -> tuple:
    return v1[:i] + v1[i+1:]

print(pop_element((1,2,3), 1)) # should print (1, 3)

#Task 5
print('Task 5')
def add(v1: tuple, v2: tuple) -> tuple:
    if len(v1) != len(v2):
        raise ValueError("error")
    else:
        return tuple(v1[i] + v2[i] for i in range(len(v1)))
try:
    print(add((1,2,3), (4,5,6))) # should print (5, 7, 9)
    print(add((1,2,3), (4,5,6,7))) # should raise error
except ValueError as e:
    print(e)
#Task 6
print('Task 6')
def dot(v1: tuple, v2: tuple) -> int:
    if len(v1) != len(v2):
        raise ValueError("error")

    return sum(v1[i] * v2[i] for i in range(len(v1)))

try:
    print(dot((1, 2, 3), (4, 5, 6)))  # should print 32
    print(dot((1, 2, 3), (4, 5, 6, 7)))  # should raise error
except ValueError as e:
    print(e)