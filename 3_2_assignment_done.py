#Task 1
print('Task 1')
def is_prime(num):
    if num == 1:
        return False
    if num <= 3:
        return True

    for d in range(2, int(num ** 0.5)+1):
        if num % d == 0:
            return False

    return True

def find_primes(a, b):
    val = []
    for i in range(a, b+1):
            if is_prime(i):
                val.append(i)
            else:
                continue
    return val

print(find_primes(1, 11))  # should print [2, 3, 5, 7, 11]

#Task 2
print('Task 2')
def find_primes_2(a, b):
    return [i for i in range(a, b+1) if is_prime(i)]

print(find_primes_2(1, 11))  # should print [2, 3, 5, 7, 11]

#Task 3
print('Task 3')
list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_out = list_in[1:10:2]

print(list_out)  # should print [1, 3, 5, 7, 9]

#Task 4
print('Task 4')
def is_even(num):
    lis = []
    lis2 = []
    for i in range(1, len(num)+1):
        if i % 2 == 0:
            lis.append(i)
        else:
            lis2.append(i)
    unsorted_list.clear()
    lis_done = lis + lis2
    for i in lis_done:
        unsorted_list.append(i)

unsorted_list = [1, 2, 3, 4, 5, 6, 7]

is_even(unsorted_list)

print(unsorted_list)  # should print [2, 4, 6, 1, 3, 5, 7] or any other valid sorting

#Task 5
print('Task 5')
terrain_map = [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]

def print_terrain_map(map):
    cols = len(map[0])
    print("+" + "-" * cols + "+") #make top + '-' multiply for length columns
    for row in map:
        line = "|" + "".join("X" if cell else " " for cell in row) + "|" #make map with join if cell is 1 X else " "
        print(line)
    print("+" + "-" * cols + "+")

print_terrain_map(terrain_map)

# Your map should look something like this:
# +----+
# |  XX|
# |   X|
# | XXX|
# |XXXX|
# +----+