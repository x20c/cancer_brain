print('Task 1')
my_set = set()
print(my_set)

print('Task 2')
sentence = "abc cba acd abc"
words =  set(sentence.split())
print(words)  # should be {'acd', 'cba', 'abc'} or in other order

print('Task 3')
sentence2 = 'cba baa acc'
words = set(words.difference(sentence2.split()))
print(words)  # should print {'acd', 'abc'} or {'abc', 'acd'}

print('Task 4')
from random import randint
N = 10000000
random_numbers = [randint(1, N) for _ in range(N)]
#Count random numbers
unique_numbers = set(random_numbers)
# Calculate the percentage of unique numbers
percentage_unique = (len(unique_numbers) / N) * 100
print(f"Percentage of unique numbers: {percentage_unique}%")
print('Task 5')
m = [
    [1, 1, 2, 3],
    [1, 2, 6, 7],
    [1, 7, 9, 9]
]
n = 2
unique_rows = [set(row) for row in m]
count = {}
for row in unique_rows:
    for value in row:
        if value not in count:
            count[value] = 0
        count[value] += 1
res = [key for key, value in count.items() if value >= n]
print(res)  # should print [1, 2, 7]